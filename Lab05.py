# Косарпур Киана - 344494 -  Вариант 4
import requests
import json
from random import randrange
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import urllib.request
import threading

def APIFunc():
    while True:
            #####################################################################
            ##########################OpenWeatherMap.org#########################


            openweathermap_Moscow = ('http://api.openweathermap.org/data/2.5/weather?'
                    'q=Moscow, RU &'
                    'appid=7cdcfaa69a322e2c77fdf3043de45290&'
                    'units=metric&'
                    'lang=ru')

            openweathermap_Saint = ('http://api.openweathermap.org/data/2.5/weather?'
                    'q=Saint Petersburg, RU&'
                    'appid=7cdcfaa69a322e2c77fdf3043de45290&'
                    'units=metric&'
                    'lang=ru')
            
            openweathermap_Tehran = ('http://api.openweathermap.org/data/2.5/weather?'
                    'q=Tehran, IR&'
                    'appid=7cdcfaa69a322e2c77fdf3043de45290&'
                    'units=metric&'
                    'lang=ru')

            openweathermap_Shiraz = ('http://api.openweathermap.org/data/2.5/weather?'
                    'q=Shiraz, IR&'
                    'appid=7cdcfaa69a322e2c77fdf3043de45290&'
                    'units=metric&'
                    'lang=ru')

            print("  ")
            print(" ************(Москва)************ ")
            print("  ")

            city = requests.get(openweathermap_Moscow)
            data = city.json()
            print("Погода в Москве:", data['weather'][0]['description'])
            print("Температура в Москве:", data['main']['temp'], "по Цельсию")
            print("Давление в Москве:", data['main']['pressure'], "гекто-паскаль")
            print("Влажность в Москве:", data['main']['humidity'], "%")

            print("  ")
            print(" ************(Петербург)************ ")
            print("  ")

            city = requests.get(openweathermap_Saint)
            data = city.json()
            print("Погода в Петербурге:", data['weather'][0]['description'])
            print("Температура в Петербурге:", data['main']['temp'], "по Цельсию")
            print("Давление в Петербурге:", data['main']['pressure'], "гекто-паскаль")
            print("Влажность в Петербурге:", data['main']['humidity'], "%")

            print("  ")
            print(" ************(Тегеран)************ ")
            print("  ")

            city = requests.get(openweathermap_Tehran)
            data = city.json()
            print("Погода в Тегеране:", data['weather'][0]['description'])
            print("Температура в Тегеране:", data['main']['temp'], "по Цельсию")
            print("Давление в Тегеране:", data['main']['pressure'], "гекто-паскаль")
            print("Влажность в Тегеране:", data['main']['humidity'], "%")

            print("  ")
            print(" ************(Шираз)************ ")
            print("  ")

            city = requests.get(openweathermap_Shiraz)
            data = city.json()
            print("Погода в Ширазе:", data['weather'][0]['description'])
            print("Температура в Ширазе:", data['main']['temp'], "по Цельсию")
            print("Давление в Ширазе:", data['main']['pressure'], "гекто-паскаль")
            print("Влажность в Ширазе:", data['main']['humidity'], "%")


            with open('openweathermap.json', 'w') as json_file01:
                json.dump(data, json_file01, indent=3)


            #####################################################################
            ########################## News API #################################


            newsapi = ('https://newsapi.org/v2/everything?'
                    'q=bbc-news&'
                    'sortBy=popularity&'
                    'apiKey=1f887eb209764fd8b75b93b0d67706dc')


            news = requests.get(newsapi)
            news = news.json()
            with open('NewsAPI.json', 'w') as json_file02:
                json.dump(news, json_file02, indent=3)





loopThread = threading.Thread(target=APIFunc, name='apifunctions')
loopThread.daemon = True  
loopThread.start()

#####################################################################
############################ Meow Generator############################

def callback():

    catURL = 'http://aws.random.cat/meow'
    imageURL = json.loads(requests.get(catURL).content)["file"]

    urllib.request.urlretrieve(imageURL, "meow.png")
    img = ImageTk.PhotoImage(Image.open("meow.png"))
    la.configure(image=img)
    la.image = img
    canvas1.itemconfig(label1_canvas, text=code)

root = Tk()
root.title("Meow Generator")
root.geometry("1024x600")


b = Button(root, text="Generate", font=("Arial", 15), command=callback)
b.grid(row=0, column=1)

la = Label(root, text="Click for genereate a cat")
la.grid(row=1, column=0)

root.mainloop()