# Web Scraping Safari – GitHub Trending Repositories

This Python script scrapes the top 5 trending repositories from [GitHub Trending](https://github.com/trending) using the `requests` and `BeautifulSoup` libraries. It extracts each repository’s name and link, and saves them into a CSV file.

## Features

-  Scrapes the GitHub Trending page
-  Extracts repository names and their URLs
-  Saves the data to a CSV file (`trending.csv`)
-  Prints the results in the terminal

## Technologies Used

- Python 
- `requests` – for sending HTTP requests
- `beautifulsoup4` – for parsing HTML
- `csv` – for writing data to CSV file

## How to Run

### 1. Clone the Repository
git clone https://github.com/KruthiSriSai/WebScrapingSafari.git
cd web-scraper
### 2. Install required Libraries
pip install requests beautifulsoup4
### 3. Run the Script
python scraper.py

After running, a trending.csv file will be created with the following columns:
Repository Name, Link






