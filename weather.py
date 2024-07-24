#!/usr/bin/env python3

import requests
from colorama import Fore, Style, Back

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
        return None

def display_weather(data):
    if not data:
        return

    # Extract relevant information from the response data
    location = data['location']['name']
    region = data['location']['region']
    country = data['location']['country']
    local_time = data['location']['localtime']
    current_condition = data['current']['condition']['text']
    temperature = data['current']['temp_c']
    humidity = data['current']['humidity']
    wind_speed = data['current']['wind_kph']
    wind_direction = data['current']['wind_dir']
    wind_degree = data['current']['wind_degree']

    # Color formatting for output
    header_color = Fore.YELLOW + Style.BRIGHT
    key_color = Fore.GREEN
    value_color = Fore.CYAN
    background_color = Back.BLACK

    # Print the information with color formatting
    print(header_color + "Weather Information:")
    print(header_color + "--------------------")
    print(key_color + "City:" + value_color + f" {location}")
    print(key_color + "Region:" + value_color + f" {region}")
    print(key_color + "Country:" + value_color + f" {country}")
    print(header_color + "----------------------------")
    print(key_color + "Local Time:" + value_color + f" {local_time}")
    print(key_color + "Condition:" + value_color + f" {current_condition}")
    print(key_color + "Temperature:" + value_color + f" {temperature}°C")
    print(key_color + "Humidity:" + value_color + f" {humidity}%")
    print(key_color + "Wind Speed:" + value_color + f" {wind_speed} kph")
    print(key_color + "Wind Direction:" + value_color + f" {wind_degree}° {wind_direction}")
    print(header_color + "---------------------------")

    # Reset color formatting
    print(Style.RESET_ALL)

if __name__ == "__main__":
    weather_data = fetch_weather()
    display_weather(weather_data)