# main.py
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        print(f"Weather in {city}: {temp}°C, {desc}")
    else:
        print("Error fetching weather data. Check city name or API key.")

def main():
    print("🌐 Weather App")
    api_key = input("Enter your OpenWeatherMap API key: ")
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ")
        if city.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        get_weather(city, api_key)

if __name__ == "__main__":
    main()
