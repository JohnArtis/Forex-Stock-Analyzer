import tkinter as tk
import WindowCommands.menu as mn
import WindowCommands.news as nw
import WindowCommands.settings as st
import WindowCommands.search as se




def gui():
    uSet = st.userSettings()
    
    #creates the main window for the GUI
    window = tk.Tk()
    canvas = tk.Frame(height = uSet.getHeight(), width = uSet.getWidth())
    mn.Menu(window, uSet)
    newsFrame = tk.Frame(canvas, height = int(uSet.getHeight() * .25), width = int( .8 * uSet.getWidth()))
    nw.News(newsFrame)
    nw.Graph(newsFrame)
    newsFrame.pack(side = tk.TOP)
    SeachFrame = tk.Frame(canvas, height = int(uSet.getHeight() * .05), width = int ( .8 * uSet.getWidth()))
    se.Search(SeachFrame)
    SeachFrame.pack( side = tk.BOTTOM)
    canvas.pack()
    window.mainloop()