import tkinter as tk
import WebScraper

#method for the searchbar
def Searchbar():
    SearchInput = tk.Entry(bd = 5)
    SearchInput.pack( side = tk.RIGHT)
    ButtonSearch = tk.Button(text ="Search")
    ButtonSearch.pack(side = tk.LEFT)

#creates the main window for the GUI
def gui():
    window = tk.Tk()
    Searchbar()
    window.mainloop()