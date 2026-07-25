import requests
city=input("Enter City:")
api_key="81986ee77ee1487279a15d9e67c6e53b"
url="https://api.openweathermap.org/data/2.5/weather?"
complete_url=url+"appid="+api_key+"&q="+city
res=requests.get(complete_url)
data=res.json()
humidity=data['main']['humidity']
pressure=data['main']['pressure']
wind=data['wind']['speed']
description=data['weather'][0]['description']
temp=data['main']['temp']
print('Temperature:',temp,'°C')
print('Wind:',wind)
print('Pressure:',pressure)
print('Humidity:',humidity)
print('Description:',description)
