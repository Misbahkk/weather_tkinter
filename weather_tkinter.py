import requests
import tkinter as tk
from PIL import ImageTk, Image 

root = tk.Tk()
root.title("Weather App")

class City:
    def __init__(self,city):
        self.city = city
        self.get_data()

    def get_data(self):
        try: 
            
            responce = requests.get( f'http://api.openweathermap.org/data/2.5/weather?units=metric&q={self.city}&appid=40f37c911820e9f79b38ca25c98f6815')
        except:
            print({"Internet issue :("})

        self.data = responce.json()
        self.temp = self.data['main']['temp']
        self.desc = self.data['weather'][0]['description']
        self.temp_min = self.data['main']['temp_min']
        self.temp_max = self.data['main']['temp_max']
        self.weather_data = {'Temparture':self.temp,'Desctription':self.desc,'tamp_max':self.temp_max,'temp_min':self.temp_min}
        update_weather_lable(self.weather_data)

# Frame for add city 
city_frame = tk.Frame(root)
city_frame.pack(padx=20,pady=30)


city_lable = tk.Label(city_frame,text="Write City Name")
city_lable.grid(row=0,column=0 ,padx=10,pady=10)
city_enter = tk.Entry(city_frame)
city_enter.grid(row=0,column=1,padx=10,pady=10)

separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=10, pady=5)
def get_weather():
    city = city_enter.get()
    city1 = City(city)
    city1.get_data()
    

weather_lable = tk.Label(root, text="Weather will be displayed")
weather_lable.pack()

def update_weather_lable(weather_data):
    weather_lable.config(text=f"Weather in {city_enter.get()}  : {weather_data['Temparture']}° C\nToday's High Temparature is: {weather_data['tamp_max']}° C\nToday's Low Temparature is: {weather_data['temp_min']}° C")
   


get_weather_button = tk.Button(city_frame, text="Get Weather", command=get_weather)
get_weather_button.grid(row=1,column=0,padx=5,pady=5)

root.mainloop()