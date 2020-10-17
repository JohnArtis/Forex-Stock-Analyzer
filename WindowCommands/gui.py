import tkinter as tk
import WindowCommands.menu as mn
import WindowCommands.news as nw




#def Graph(self, graph):
    #show current Market and show a projected output



def gui():
    #creates the main window for the GUI
    window = tk.Tk()
    canvas = tk.Canvas(window, height = 1280, width = 1024)
    mn.Menu(window)
    nw.News(window)
    canvas.pack()
    window.mainloop()