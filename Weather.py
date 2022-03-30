# Imported Modules
import requests

# Global Variables
count = 0
lon = []
lat = []
# API key goes here! This program uses open-weather for its free API.
api_key = "ENTER API KEY HERE"
# I used the US for this example program, but you can put any countries initials here.
country = "us"


def user_zip():
    # Here we begin to receive input from the user, while also looping back on unknown zipcodes.
    while count == 0:
        user_zipcode = input("\nEnter your zipcode for weather in your area.:")
        url_lat = f"http://api.openweathermap.org/geo/1.0/zip?zip={user_zipcode},{country}&appid={api_key}"
        response_lat_check = requests.get(url_lat).status_code
        if response_lat_check == 200:
            response = requests.get(url_lat).json()
            lon.append(response["lon"])
            lat.append(response["lat"])
            break
        else:
            print("\nSorry I didn't understand that. Let's try that again.")


user_zip()


url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat[0]}&lon={lon[0]}&appid={api_key}&units=imperial"
response_weather = requests.get(url_weather).json()
temp = response_weather["main"]["temp"]
temp_feel = response_weather["main"]["feels_like"]
humidity = response_weather["main"]["humidity"]
temp = int(temp)
temp_feel = int(temp_feel)
name_place = response_weather["name"]

print("\nIn", name_place, "it is currently:", temp, "degrees fahrenheit, it feels like:", temp_feel,
      "degrees fahrenheit, and the humidity is:", humidity, "%")
