#Importing the libraries
import requests

def getLatitudeLongitude():
    latitude = (input("Enter the latitude"))
    longitude = (input("Enter the longitude"))
    triggerWeatherAPI(latitude, longitude)

def triggerWeatherAPI(latitude, longitude):
    url = "http://api.openweathermap.org/data/2.5/weather?"+ "lat="+(latitude)+"&lon="+(longitude) + "&appid=" + "f192cd7f393c4e0a500e763ee96e6313" + "&units=metric"
    res = requests.get(url)
    data = res.json()
    print(data)
    displayGenericWeather(data)

def displayGenericWeather(data):
    print("Weather: .{}".format(data["weather"][0]["description"]), "\n")
    print("Temperature: .{}".format(data["main"]["temp"]), "\n")
    print("Temperature Min: .{}".format(data["main"]["temp_min"]), "\n")
    print("Temperature Max: .{}".format(data["main"]["temp_max"]), "\n")
    print("Pressure: .{}".format(data["main"]["pressure"]), "\n")
    print("Humidity: .{}".format(data["main"]["humidity"]), "\n")
    print("Sunrise: .{}".format(data["sys"]["sunrise"]), "\n")
    print("Sunset: .{}".format(data["sys"]["sunset"]), "\n")
    print("City name: .{}".format(data["name"]), "\n")
    forecastWeatherInDay(data["name"])

def forecastWeatherInDay(city):
    url = "https://wttr.in/" + city
    data = requests.get(url)
    print(data.text)

if __name__ == "__main__":
    getLatitudeLongitude()