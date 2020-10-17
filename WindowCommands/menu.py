import tkinter as tk
import WindowCommands.settings as st

def changeResolution(x):
    #change the Resolution of the program
    uSet = st.userSettings()
    if(x == 0):
        uSet.setHeight(1280)
        uSet.setWidth(1024)
    elif(x == 1):
        uSet.setHeight(1600)
        uSet.setWidth(1280)
    elif(x == 2):
        uSet.setHeight(1680)
        uSet.setWidth(1050)
    elif(x == 3):
        uSet.setHeight(1280)
        uSet.setWidth(1024)
    elif(x == 4):
        uSet.setHeight(1280)
        uSet.setWidth(1024)

def reSize(windwow):
    screen19 = tk.Button(text = "1280 x 1024", command = changeResolution(0))
    screen20 =  tk.Button(text = "1600 x 1200", command = changeResolution(1))
    screen22 =  tk.Button(text = "1680 x 1050", command = changeResolution(2))
    screenUltrawide =   tk.Button(text = "1280 x 1024", command = changeResolution(3))
    screenDefault = tk.Button(text = "default", command = changeResolution(4))
    

def printPage():
    #output the current screen to a word document
    print("Will be used to output the current screen to a word document")
def Menu(window):
    #user able to access settings for the window along with generate their own report
    menuBar = tk.Menu(window)

    fileMenu = tk.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label = "File", menu = fileMenu)

    printMenu = tk.Menu(menuBar,tearoff=0)
    menuBar.add_cascade(label = "Print", menu = printMenu)
    printMenu.add_command(label = "Print", command = printPage)
    settingMenu = tk.Menu(menuBar, tearoff=0)
    settingMenu.add_command(label = "Options", command = reSize(window))
    menuBar.add_cascade(label = "Settings", menu = settingMenu)
    
    
    window.config(menu = menuBar)