import requests
from colorama import Fore, Style

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q": "6.2644,100.4202"}

headers = {
    "X-RapidAPI-Key": "f0a9fe3871msh192738b40e662a5p161f15jsnf33c0a9f0c1b",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()

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

# Print the information with color formatting
print(header_color + "Weather Information:")
print(header_color + "--------------------")
print(key_color + "City:" + value_color, location)
print(key_color + "Region:" + value_color, region)
print(key_color + "Country:" + value_color, country)
print(header_color + "----------------------------")
print(key_color + "Local Time:" + value_color, local_time)
print(key_color + "Condition:" + value_color, current_condition)
print(key_color + "Temperature:" + value_color, f"{temperature}°C")
print(key_color + "Humidity:" + value_color, f"{humidity}%")
print(key_color + "Wind Speed:" + value_color, f"{wind_speed} kph")
print(key_color + "Wind Direction:" + value_color, f"{wind_degree}° {wind_direction}")
print(header_color + "---------------------------")

# Reset color formatting
print(Style.RESET_ALL)
