import tkinter as tk
def hello():
    print("hello")

def News(window):
    #will scrape the web for elevent News 
    newsFrame = tk.Canvas(window, height = 500, width = 300)
    
    newsFrame.pack()