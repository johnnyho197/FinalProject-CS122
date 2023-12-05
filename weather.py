from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import requests
import pytz
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from PIL import Image, ImageTk

root=Tk()
root.title("Weather App")
root.geometry("900x700+300+200")
root.resizable(False, False)
home = None
daily_info = {}

def getWeather():
    global home
    global daily_info
    try:
    
        city=textfield.get()
        geolocator = Nominatim(user_agent="weather")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%A %I:%M %p")
        clock.config(text=current_time)
        name.config(text="Current Time - Weather")

        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=661e005c7ad0170cde8de06ee933910d"
        forecast_api = "https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=661e005c7ad0170cde8de06ee933910d"

        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        feels_like = int(json_data['main']['feels_like'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°C"))
        c.config(text=(condition, "|", "FEELS", "LIKE", feels_like,"°C"))
        w.config(text=(wind,"m/s"))
        h.config(text=humidity)
        d.config(text=(description.title()))
        p.config(text=pressure)
        
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid City Name")
        
#Search box        
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=365,y=34)

#Logo
Logo_image=PhotoImage(file="Weather_logo.png")
logo=Label(image=Logo_image)
logo.place(x=10,y=120)

#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",10,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("arial",15))
clock.place(x=30,y=130)

#label
label1 = Label(root, text="Wind Speed", font=("Arial", 15, 'bold'), fg="white", bg="#16d5f1")  # Corrected color code
label1.place(x=50, y=625)

label2 = Label(root, text="Humidity", font=("Arial", 15, 'bold'), fg="white", bg="#16d5f1")  # Corrected color code
label2.place(x=250, y=625)

label3 = Label(root, text="Description", font=("Arial", 15, 'bold'), fg="white", bg="#16d5f1")  # Corrected color code
label3.place(x=430, y=625)

label4 = Label(root, text="Pressure", font=("Arial", 15, 'bold'), fg="white", bg="#16d5f1")  # Corrected color code
label4.place(x=650, y=625)

t=Label(font=("arial",50,"bold"),fg="#EC9EC0")
t.place(x=400,y=180)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=280)

w=Label(text="...",font=("arial",15,"bold"),bg="#16d5f1")
w.place(x=75,y=650)
h=Label(text="...",font=("arial",15,"bold"),bg="#16d5f1")
h.place(x=280,y=650)
d=Label(text="...",font=("arial",15,"bold"),bg="#16d5f1")
d.place(x=460,y=650)
p=Label(text="...",font=("arial",15,"bold"),bg="#16d5f1")
p.place(x=670,y=650)

root.mainloop()