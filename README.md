# basic_web_scraping
A basic web scraping begginer program showcasing how to scrape data from a website.Here it is done from wiki pedia and then the to csv simply said A simple Python project that scrapes the top 50 highly-ranked films from an archived wiki page, processes the data using BeautifulSoup and Pandas, and saves the output to a CSV file and a SQLite database.
This script extracts information about top-rated movies, specifically:
- Average Rank
- Film Title
- Release Year

Once scraped, the data is cleaned and stored in two formats:
1. **CSV File:** `top_50_films.csv`
2. **SQLite Database:** `Movies.db` (Table: `Top_50`)

---

## 🛠️ Requirements & Installation

Make sure you have Python installed on your system. You will need to install the following libraries before running the script:

```bash
pip install requests pandas beautifulsoup4
