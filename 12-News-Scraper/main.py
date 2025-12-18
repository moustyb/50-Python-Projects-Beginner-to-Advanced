# main.py
import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            headlines = soup.find_all("h2")  # adjust tag based on site
            print("\nTop Headlines:")
            for h in headlines[:10]:  # limit to first 10
                print("-", h.get_text(strip=True))
        else:
            print("Error fetching page:", response.status_code)
    except Exception as e:
        print("Error:", e)

def main():
    print("📰 News Scraper")
    url = input("Enter news site URL (e.g., https://www.bbc.com): ")
    fetch_headlines(url)

if __name__ == "__main__":
    main()
