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

### Deployed in Render (Recommended)

## Live Link : https://websrcapper-pro.onrender.com/

## License

MIT License
