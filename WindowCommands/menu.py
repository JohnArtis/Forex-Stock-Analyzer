import tkinter as tk
import WindowCommands.settings as st

def changeResolution(x, userSetting):
    #change the Resolution of the program
    if(x == 0):
        userSetting.setHeight(1280)
        userSetting.setWidth(1024)
    elif(x == 1):
        userSetting.setHeight(1600)
        userSetting.setWidth(1280)
    elif(x == 2):
        userSetting.setHeight(1680)
        userSetting.setWidth(1050)
    elif(x == 3):
        userSetting.setHeight(1280)
        userSetting.setWidth(1024)
    elif(x == 4):
        userSetting.setHeight(1280)
        userSetting.setWidth(1024)
    


def printPage():
    #output the current screen to a word document
    print("Will be used to output the current screen to a word document")
def Menu(window, userSetting):
    #user able to access settings for the window along with generate their own report
    menuBar = tk.Menu(window)
    
    fileMenu = tk.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label = "File", menu = fileMenu)

    printMenu = tk.Menu(menuBar,tearoff=0)
    menuBar.add_cascade(label = "Print", menu = printMenu)
    printMenu.add_command(label = "Print", command = printPage)
    settingMenu = tk.Menu(menuBar, tearoff=0)
    settingMenu.add_command(label = "1280 x 1024", command = changeResolution(0, userSetting))
    settingMenu.add_command(label = "1600 x 1200", command = changeResolution(1, userSetting))
    settingMenu.add_command(label = "1680 x 1050", command = changeResolution(2, userSetting))
    settingMenu.add_command(label = "1280 x 1024", command = changeResolution(3, userSetting))
    settingMenu.add_command(label = "default", command = changeResolution(4, userSetting))

    menuBar.add_cascade(label = "Settings", menu = settingMenu)
    
    
    window.config(menu = menuBar)