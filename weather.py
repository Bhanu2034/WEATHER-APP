import requests
import pprint

api_key = "216525c0a871374f9684cf4105302f90"  # Replace with your actual API key
city = input("Enter a city name: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(complete_url)
data = response.json()

# Check for errors
if data["cod"] != 200:
    print("Error: City not found")
else:
    # Print relevant weather information
    main = data["main"]
    weather = data["weather"][0]
    print("**Current Weather in", city, "**")
    print("Temperature:", main["temp"] - 273.15, "°C")  # Convert Kelvin to Celsius
    print("Description:", weather["description"])
    print("Humidity:", main["humidity"], "%")
