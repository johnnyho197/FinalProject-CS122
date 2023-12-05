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
        
<<<<<<< HEAD
        plot_button = Button(root, text="Temperatures in the next 10 hours", command=plot_temperatures)
        plot_button.place(x=500, y=350)

        json_forecast_data = requests.get(forecast_api).json()
        
        daily_info = {}
        for entry in json_forecast_data['list']:
            timestamp = entry['dt']
            forecast_time_utc = datetime.utcfromtimestamp(timestamp)
            forecast_time = forecast_time_utc.replace(tzinfo=pytz.utc).astimezone(home)
            day = forecast_time.strftime("%A")
            temp_min = int(entry['main']['temp_min'] - 273.15)
            temp_max = int(entry['main']['temp_max'] - 273.15)
            icon_url = entry['weather'][0]['icon']

            if day not in daily_info:
                daily_info[day] = {'min': temp_min, 'max': temp_max, 'icon_url': icon_url}
            else:
                daily_info[day]['min'] = min(daily_info[day]['min'], temp_min)
                daily_info[day]['max'] = max(daily_info[day]['max'], temp_max)

        update_forecast_labels()
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid City Name")
        

def plot_temperatures():
    global home
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="weather")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        current_time = datetime.now(home)

        api_hourly = "https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=661e005c7ad0170cde8de06ee933910d"
        json_hourly_data = requests.get(api_hourly).json()

        hourly_temps = []
        timestamps = []

        for entry in json_hourly_data['list'][:10]:
            timestamp = entry['dt']
            forecast_time_utc = datetime.utcfromtimestamp(timestamp)
            
            forecast_time = forecast_time_utc.replace(tzinfo=pytz.utc).astimezone(home)

            time_difference = (forecast_time - current_time).total_seconds() / 3600

            if 0 <= time_difference <= 10:
                timestamps.append(forecast_time)
                temp = int(entry['main']['temp'] - 273.15)
                hourly_temps.append(temp)

        interp_function = interp1d([t.timestamp() for t in timestamps], hourly_temps, kind='linear', fill_value='extrapolate')
        interpolated_timestamps = [current_time + timedelta(hours=i) for i in range(11)] 
        interpolated_temps = interp_function([t.timestamp() for t in interpolated_timestamps])

        plt.figure(figsize=(10, 5))
        plt.plot_date([t.strftime('%H:%M') for t in interpolated_timestamps], interpolated_temps, 'o-', color='b')
        plt.title(f'Hourly Temperatures for the Next 10 Hours in {city.title()}')
        plt.xlabel('Time')
        plt.ylabel('Temperature (°C)')

        for i, txt in enumerate(interpolated_temps):
            plt.annotate(f'{txt:.2f}°C', (interpolated_timestamps[i].strftime('%H:%M'), interpolated_temps[i]), textcoords="offset points", xytext=(0, 10), ha='center')

        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Weather App", "Failed to plot temperatures")

def update_forecast_labels():
    day_labels = [day1, day2, day3, day4, day5, day6]
    image_labels = [firstimage, secondimage, thirdimage, forthimage, fifthimage, sixthimage]

    for i, (day, info) in enumerate(daily_info.items()):
        
        day_labels[i]['text'] = f"{day}\nMin Temp: {info['min']}°C\n Max Temp: {info['max']}°C"

        icon_image = (Image.open(f"images/{info['icon_url']}@2x.png"))
        resized_img = icon_image.resize((40,40))
        photo = ImageTk.PhotoImage(resized_img)
        image_labels[i].config(image=photo)
        image_labels[i].image = photo
        
=======
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid City Name")
        
#Search box        
>>>>>>> 4100556c2cf473285d7a2ed5ed3576d33578a25c
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

<<<<<<< HEAD
# 5 day-forecast box
frame = Frame(root, width=200, height=750, bg="#212120")
frame.pack(side=RIGHT)

firstframe = Frame(root, width=160,height=80, bg="#282829")
firstframe.place(x=722,y=33)
day1 = Label(firstframe, font="arial 12", bg="#282829",fg="#fff")
day1.place(x=35, y=5)
firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=0, y=15)

secondframe = Frame(root, width=160,height=60, bg="#282829")
secondframe.place(x=722,y=153)
day2 = Label(secondframe, font="arial 10", bg="#282829", fg="#fff")
day2.place(x=40, y=5)
secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=1, y=15)

thirdframe = Frame(root, width=160,height=60, bg="#282829")
thirdframe.place(x=722,y=233)
day3 = Label(thirdframe, font="arial 10", bg="#282829", fg="#fff")
day3.place(x=40, y=5)
thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=1, y=15)

forthframe = Frame(root, width=160,height=60, bg="#282829")
forthframe.place(x=722,y=313)
day4 = Label(forthframe, font="arial 10", bg="#282829", fg="#fff")
day4.place(x=40, y=5)
forthimage = Label(forthframe, bg="#282829")
forthimage.place(x=1, y=15)

fifthframe = Frame(root, width=160,height=60, bg="#282829")
fifthframe.place(x=722,y=393)
day5 = Label(fifthframe, font="arial 10", bg="#282829", fg="#fff")
day5.place(x=40, y=5)
fifthimage = Label(fifthframe, bg="#282829")
fifthimage.place(x=1, y=15)

sixthframe = Frame(root, width=160,height=60, bg="#282829")
sixthframe.place(x=722,y=473)
day6 = Label(sixthframe, font="arial 10", bg="#282829", fg="#fff")
day6.place(x=40, y=5)
sixthimage = Label(sixthframe, bg="#282829")
sixthimage.place(x=1, y=15)

root.mainloop()
=======
root.mainloop()
>>>>>>> 4100556c2cf473285d7a2ed5ed3576d33578a25c
