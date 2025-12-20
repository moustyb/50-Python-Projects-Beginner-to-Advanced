# main.py

import requests
import matplotlib.pyplot as plt

API_URL = "https://api.coindesk.com/v1/bpi/historical/close.json"

def fetch_data():
    print("Fetching stock data...")
    response = requests.get(API_URL)
    data = response.json()
    return data["bpi"]

def plot_data(prices):
    dates = list(prices.keys())
    values = list(prices.values())

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker="o")
    plt.title("Stock Price Tracker (Demo Bitcoin Data)")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    print("📈 Stock Price Tracker")
    print("This demo uses Bitcoin price data (no API key needed).")

    prices = fetch_data()
    print("✅ Data fetched successfully.")

    plot_data(prices)

if __name__ == "__main__":
    main()
