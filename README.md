# Weather Forecasting Application

## Goal
* The application is built in python. It takes in two values as input latitude and longitude and returns the corresponding weather details of that location including weather details at a given point in day like 
afternoon, morning, night.


## Libraries / Modules Required:
* requests: pip install requests

## Public API used: https://openweathermap.org


## Steps to follow to get the API key to access the API
* https://openweathermap.org/api > API > Register > Get the API Key
* For the present application you can use the key : f192cd7f393c4e0a500e763ee96e6313
*The API key was already received before the presentation and can be reused during testing the application.
*Note: In ideal scenarios, its not a good practice to store credentials / keys in code


## Methods / Functionalities

| Method Name                     | What does it do?                                                    |
| -------------                   |:-------------:                                                      |
| getLatitudeLongitude()          | Takes latitude and longitude as input                               |
| triggerWeatherAPI():            | Hits the public API as mentioned above and receives response in the form of JSON                                                                                                    |
| displayGenericWeather()         | The method returns / prints respective weather details of that location by parsing the JSON response                                                                                |
| forecastWeatherInDay():         | The method shows the weather forecast of that location at various phases of a day like night, noon, morning                                                                             |