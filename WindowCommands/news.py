import tkinter as tk
import WindowCommands.search as sch
import WindowCommands.settings as st
#The News Frame will scrape the internet for Relevant Forex News depending on the users search.


def hello():
    print("hello")

def News(window):
    uSet = st.userSettings()
    #will scrape the web for elevent News 
    newsFrame = tk.Frame(window, bg = "green", height = int(.5 * uSet.getHeight()), width = int(.5 * uSet.getWidth()))
    
    newsFrame.pack()