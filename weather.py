import requests

# Enter your API key here
api_key = '6f7f39550cde4de4894113247220112'

# base_url variable to store url
base_url = 'http://api.weatherapi.com/v1/current.json'

# Give city name
city_name = input('Enter city name : ')


complete_url = base_url + '?key=' + api_key + '&q=' + city_name
print(complete_url)

response = requests.get(complete_url)

if response.status_code == 200:
    data = response.json()
    current = data['current']

    current_temperature = current['temp_c']
    current_wind = current['wind_kph']
    current_pressure = current['pressure_in']
    # weather_report = data['weather']

    # print following values
    print(f" Temperature (in centigrade) = " + str(current_temperature) +
          "\n atmospheric pressure = " + str(current_pressure) +
          "\n wind (in km/h) = " + str(current_wind))

else:
    print(" City Not Found ")
