import tkinter as tk
import WebScraper

#method for Menu Bar
def MenuBar():
    wMenu = tk.Menu(window)
    filemenu = tk.Menu(wMenu, tearoff = 0)
    filemenu.add_command(label = "Print", command = null)
    wMenu.add_cascade(label = "File", menu = filemenu)
#method for News Frame
def NewsFrame():
    News = tk.Menu


#method for Graph Frame outputs the stock Market
#def GraphFrame():
    #Graph =


#method for the Searchbar
def Searchbar():
    SearchInput = tk.Entry(bd = 5)
    SearchInput.pack( side = tk.RIGHT)
    ButtonSearch = tk.Button(text ="Search")
    ButtonSearch.pack(side = tk.LEFT)

#creates the main window for the GUI
def gui():
    window = tk.Tk()
    MenuBar()
    Searchbar()
    #GraphFrame()
    #NewsFrame()
    window.mainloop()