import tkinter as tk
import WindowCommands.search as sch
import WindowCommands.settings as st
import GUI.WebScraper as ws


def hello():
    print("hello")

def News(window):
    
    
    
    uSet = st.userSettings()
    #Left side will consist of active stock spreads eg: AAPL and such
    newsFramel = tk.Canvas(window, bg = "green", height = int(.25 * uSet.getHeight()), width = int(.23 * uSet.getWidth()) )
    ws.outPut(newsFramel, 1)
    newsFramel.pack(side = tk.LEFT)


    #News Frame split into two sides right side will consist of active currency spreads
    newsFramer = tk.Canvas(window, bg = "green", height = int(.25 * uSet.getHeight()), width = int(.23 * uSet.getWidth()) )
    ws.outPut(newsFramer, 0)
    newsFramer.pack(side = tk.RIGHT)