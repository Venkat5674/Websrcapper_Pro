from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers, verify=True)
            response.raise_for_status()  # Raise an exception for bad status codes
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract basic information
            title = soup.title.string if soup.title else 'No title found'
            meta_desc = soup.find('meta', {'name': 'description'})
            meta_description = meta_desc['content'] if meta_desc and 'content' in meta_desc.attrs else 'No description found'

            # Clean and process headings
            headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3']) if h.get_text(strip=True)]

            # Process links - convert relative URLs to absolute
            links = []
            for a in soup.find_all('a', href=True):
                href = a.get('href')
                if href and not href.startswith(('#', 'javascript:')):
                    absolute_url = urljoin(url, href)
                    text = a.get_text(strip=True) or absolute_url
                    links.append({'text': text, 'href': absolute_url})

            # Process images - convert relative URLs to absolute
            images = []
            for img in soup.find_all('img', src=True):
                src = img.get('src')
                if src and not src.startswith('data:'):
                    absolute_src = urljoin(url, src)
                    alt = img.get('alt', '').strip()
                    images.append({'src': absolute_src, 'alt': alt})

            data = {
                'title': title,
                'meta_description': meta_description,
                'headings': headings,
                'links': links,
                'images': images
            }
            return jsonify(data)
        except requests.RequestException as e:
            return jsonify({'error': f'Failed to fetch the URL: {str(e)}'}), 400
        except Exception as e:
            return jsonify({'error': f'An error occurred: {str(e)}'}), 400
    
    return render_template('scrape.html')

if __name__ == '__main__':
    import os
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
