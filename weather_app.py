import requests

def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)
    data = response.json()
    
    if "results" not in data:
        return None, None

    result = data["results"][0]
    return result["latitude"], result["longitude"]

def get_weather(lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )
    response = requests.get(url)
    data = response.json()
    return data["current_weather"]

def main():
    print("🌤️  Weather App - CLI")
    city = input("Enter city name: ")

    lat, lon = get_coordinates(city)
    if lat is None:
        print("❌ City not found.")
        return

    weather = get_weather(lat, lon)
    print(f"\nWeather in {city.capitalize()}:")
    print(f"🌡️ Temperature: {weather['temperature']}°C")
    print(f"💨 Wind Speed: {weather['windspeed']} km/h")
    print(f"🧭 Wind Direction: {weather['winddirection']}°")
    print(f"📅 Time: {weather['time']}")

if __name__ == "__main__":
    main()
