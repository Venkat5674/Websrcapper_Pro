# Web Scraper Pro

A modern web-based scraping tool built with Flask and a beautiful UI. This application allows users to extract valuable information from any webpage with ease.

## Features

- Modern, responsive UI with animations
- Extract page titles and meta descriptions
- Collect all links and headings
- Find and download images
- Real-time scraping with loading indicators
- Beautiful gradient design elements

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows:
     ```
     .\venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```
     source venv/bin/activate
     ```
4. Install dependencies:
   ```
   pip install flask beautifulsoup4 requests
   ```

## Running the Application

1. Activate the virtual environment (if not already activated)
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open your browser and navigate to `http://localhost:5000`

## Technologies Used

- Backend:
  - Flask (Python web framework)
  - BeautifulSoup4 (HTML parsing)
  - Requests (HTTP client)

- Frontend:
  - TailwindCSS (Styling)
  - AOS (Animate On Scroll library)
  - Modern JavaScript (ES6+)

## Usage

1. Navigate to the home page
2. Click "Start Scraping" to go to the scraping interface
3. Enter a URL you want to scrape
4. Click "Start Scraping" and wait for the results
5. View the extracted information in a beautiful, organized layout

## Deployment

### PythonAnywhere (Recommended)

1. Sign up for a [PythonAnywhere account](https://www.pythonanywhere.com)
2. Go to the Dashboard and click on "Web" tab
3. Click "Add a new web app"
4. Choose "Flask" as your web framework
5. Select "Python 3.8" or higher
6. Set up your source code:
   - Upload your files using the Files tab
   - Or use Git to clone your repository
7. Update your WSGI configuration file with:
   ```python
   import sys
   path = '/home/yourusername/Python_webscrapper'
   if path not in sys.path:
       sys.path.append(path)
   
   from wsgi import app as application
   ```
8. Install requirements:
   ```bash
   pip3 install -r requirements.txt
   ```
9. Reload your web app

### Environment Setup

Make sure to set these environment variables in production:
- `FLASK_ENV=production`
- `FLASK_SECRET_KEY=your-secret-key`

### Security Considerations

1. Ensure DEBUG mode is disabled
2. Use HTTPS in production
3. Set proper rate limiting for the scraping endpoint
4. Configure error handling

## License

MIT License
