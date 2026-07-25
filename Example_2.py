from tkinter import*
from tkinter import messagebox
import requests
def get_weather():
    city=city_entry.get()
    api_key=""
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

top=Tk()
Label(top,text="City Name:").grid(row=0,column=1,sticky=W,pady=4)
city_entry=Entry(top)
city_entry.grid(row=0,column=2)
Button(top,text="get_weather",command=get_weather).grid(row=0,column=3,stick=W,pady=4)
mainloop()

