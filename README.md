# 🕷️ Web Scraping

A collection of web-scraping and browser automation projects built using Python, Requests, BeautifulSoup, Selenium, and APIs to extract, process, and automate tasks on websites.

## 🚀 Projects

| Project | Description | Technologies |
|---|---|---|
| 🎬 [Movie Scraper](./Movie-Scraper) | Scrapes a ranked list of movies from an archived Empire Online page and saves the results to a text file. | Python, Requests, BeautifulSoup |
| 🎵 [Billboard Spotify](./Billboard-Spotify) | Scrapes Billboard's Hot 100 chart for a selected date and creates a Spotify playlist containing the available songs. | Python, Requests, BeautifulSoup, Spotipy |
| 💰 [Amazon Price Tracker](./Amazon-Price-Tracker) | Scrapes an Amazon product page, checks its price against a target value, and sends an email alert when the price drops below it. | Python, Requests, BeautifulSoup, SMTP |
| 🍪 [Cookie Clicker](./Cookie-Clicker) | Automates Cookie Clicker by clicking the cookie, detecting available upgrades, purchasing items, and tracking the final cookie count and production rate. | Python, Selenium |
| 💼 [LinkedIn Job Automation](./LinkedIn-Job-Automation) | Automates the LinkedIn job application process by logging in, browsing job listings, attempting simple applications, and skipping complex applications. | Python, Selenium |
| 🏠 [Zillow Property Scraper](./Zillow-Property-Scraper) | Scrapes property listings from a Zillow clone and automatically submits the collected addresses, prices, and links to a Google Form. | Python, Requests, BeautifulSoup, Selenium |

## 🛠️ Technologies

- Python
- Requests
- BeautifulSoup
- Selenium
- Spotipy
- Spotify Web API
- SMTP
- Google Forms
- Web Scraping
- HTML Parsing
- Browser Automation
- API Integration

## 📂 Repository Structure

```text
Web-Scraping/
├── Movie-Scraper/
│   ├── main.py
│   └── movies.txt
│
├── Billboard-Spotify/
│   └── main.py
│
├── Amazon-Price-Tracker/
│   └── main.py
│
├── Cookie-Clicker/
│   └── main.py
│
├── LinkedIn-Job-Automation/
│   └── main.py
│
├── Zillow-Property-Scraper/
│   └── main.py
│
├── .gitignore
└── README.md