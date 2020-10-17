import tkinter as tk


def reSize():
    print("Work in progress")

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
    settingMenu.add_command(label = "Options", command = reSize)
    menuBar.add_cascade(label = "Settings", menu = settingMenu)
    
    
    window.config(menu = menuBar)