import tkinter as tk
import requests
from tkinter import messagebox

API_KEY = "1a73317e2d07da1cd2efc97eaea722a1"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Enter city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
    
        result_label.config(
           text=f"📍 City: {city}\n\n🌡 Temp: {temp}°C\n☁ Weather: {weather}\n💧 Humidity: {humidity}%"
        )

    except:
        messagebox.showerror("Error", "Failed to fetch data")



# GUI Window
root = tk.Tk()
root.title("🌦 Weather App")
root.geometry("420x400")
root.configure(bg="#1e1e2f")  # Dark background

# Title
title_label = tk.Label(
    root,
    text="Weather App",
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title_label.pack(pady=20)

# City Input
tk.Label(
    root,
    text="Enter City",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="lightgray"
).pack()

city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25,
    justify="left"
)
city_entry.pack(pady=10)

# Button
tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    command=get_weather
).pack(pady=15)

# Result Box
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 13),
    bg="#2c2c3e",
    fg="white",
    width=35,
    height=6,
    justify="left",
    relief="ridge",
    bd=2
)
result_label.pack(pady=20)

root.mainloop()