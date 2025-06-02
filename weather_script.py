import requests

def fetch_weather(city_name, api_key):
    """
    Fetches weather data for a given city from the OpenWeatherMap API.

    Args:
        city_name (str): Name of the city.
        api_key (str): Your OpenWeatherMap API key.

    Returns:
        dict: Weather data as a dictionary, or None if request fails.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")
    weather = fetch_weather(city, api_key)
    if weather:
        print(f"Weather in {city}: {weather['weather'][0]['description'].capitalize()}, Temperature: {weather['main']['temp']}°C")
    else:
        print("Failed to fetch weather data.")