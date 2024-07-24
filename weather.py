#!/usr/bin/env python3

import requests
from colorama import Fore, Style

# Constants
URL = "https://weatherapi-com.p.rapidapi.com/current.json"
QUERYSTRING = {"q": "53.1,-0.13"}  # Change the latitude and longitude based on where you live
HEADERS = {
    "X-RapidAPI-Key": "Your-Api-Key",  # Replace with your actual API key
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

def fetch_weather():
    try:
        response = requests.get(URL, headers=HEADERS, params=QUERYSTRING)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "An error occurred while fetching weather data: " + str(e))
        print(Fore.YELLOW + "Please ensure you have replaced 'Your-Api-Key' with a valid API key.")
        print(Fore.YELLOW + "You can obtain an API key by signing up at: https://rapidapi.com/weatherapi/api/weatherapi-com")
        return None

def display_weather(data):
    if not data:
        print(Fore.RED + "No data available to display.")
        return

    # Extract relevant information from the response data
    location = data.get('location', {}).get('name', 'N/A')
    region = data.get('location', {}).get('region', 'N/A')
    country = data.get('location', {}).get('country', 'N/A')
    local_time = data.get('location', {}).get('localtime', 'N/A')
    current_condition = data.get('current', {}).get('condition', {}).get('text', 'N/A')
    temperature = data.get('current', {}).get('temp_c', 'N/A')
    humidity = data.get('current', {}).get('humidity', 'N/A')
    wind_speed = data.get('current', {}).get('wind_kph', 'N/A')
    wind_direction = data.get('current', {}).get('wind_dir', 'N/A')
    wind_degree = data.get('current', {}).get('wind_degree', 'N/A')

    # Color formatting for output
    header_color = Fore.YELLOW + Style.BRIGHT
    key_color = Fore.GREEN + Style.BRIGHT
    value_color = Fore.CYAN + Style.BRIGHT
    border_color = Fore.MAGENTA + Style.BRIGHT

    # Print the information with color formatting
    print(border_color + "=" * 50)
    print(header_color + " Weather Information ".center(50, "="))
    print(border_color + "=" * 50)
    print(f"{key_color}City:".ljust(25) + f"{value_color}{location}".rjust(25))
    print(f"{key_color}Region:".ljust(25) + f"{value_color}{region}".rjust(25))
    print(f"{key_color}Country:".ljust(25) + f"{value_color}{country}".rjust(25))
    print(border_color + "-" * 50)
    print(f"{key_color}Local Time:".ljust(25) + f"{value_color}{local_time}".rjust(25))
    print(f"{key_color}Condition:".ljust(25) + f"{value_color}{current_condition}".rjust(25))
    print(f"{key_color}Temperature:".ljust(25) + f"{value_color}{temperature}°C".rjust(25))
    print(f"{key_color}Humidity:".ljust(25) + f"{value_color}{humidity}%".rjust(25))
    print(f"{key_color}Wind Speed:".ljust(25) + f"{value_color}{wind_speed} kph".rjust(25))
    print(f"{key_color}Wind Direction:".ljust(25) + f"{value_color}{wind_degree}° {wind_direction}".rjust(25))
    print(border_color + "=" * 50)

    # Reset color formatting
    print(Style.RESET_ALL)

if __name__ == "__main__":
    print(Fore.GREEN + "Fetching weather data...")
    weather_data = fetch_weather()
    display_weather(weather_data)