from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox

url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']

def getWeather(city):
    result = requests.get(url.format(city, api_key))

    if result.status_code == 200:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_celsius, weather1]
        return final
    else:
        print("Error in the HTTP request")

def search():
    city = cityText.get()
    weather = getWeather(city)
    if weather:
        location_lbl['text'] = f"{weather[0]}, {weather[1]['country']}"
        temperature_lbl['text'] = f"{weather[2]:.2f} °C"
        weather_l['text'] = weather[3]
    else:
        messagebox.showerror("Error", "Could not retrieve weather data")

app = Tk()
app.title("Weather App")

cityText = StringVar()
city_entry = Entry(app, textvariable=cityText)
city_entry.pack()

Search_btn = Button(app, text="Search Weather", command=search)
Search_btn.pack()

location_lbl = Label(app, text="", font=("bold", 20))
location_lbl.pack()

temperature_lbl = Label(app, text="")
temperature_lbl.pack()

weather_l = Label(app, text="")
weather_l.pack()

app.mainloop()