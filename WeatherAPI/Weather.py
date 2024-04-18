import requests

API_KEY = "d3b457859279cfcd7d7eedeee1180d09"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name:")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    weather = data['weather'][0]["description"]
    print("Weather :", weather.upper())
    temperature = data["main"]["temp"]
    c_temperature = round(data["main"]["temp"] - 273.15, 2)  # to conver to celcius
    print("Temperature in Celcius:", c_temperature)
    print("Temperature in Farenheit:", temperature)

    T_min = data["main"]["temp_min"]
    T_max = data["main"]["temp_max"]
    print("Temperature minimum:", T_min)
    print("Temperature maximum:", T_max)

    humidity = data["main"]["humidity"]
    visibility = data["visibility"]
    print("Humidity:", humidity)
    print("Visibility:", visibility)


else:
    print("An Error Occured, try again with proper city name")
