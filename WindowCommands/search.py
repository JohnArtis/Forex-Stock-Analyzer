import tkinter as tk
import WindowCommands.settings as st
import GUI.WebScraper as ws
import re
class search(object):
    def __init__(self, stockName, userSearch):
        self.stockName = stockName
        self.userSearch = userSearch
        

    def getStockName(self):
        return self.stockName

    def getUserSearch(self):
        return self.userSearch

    def setStockName(self, x):
        self.stockName = x

    def setUserSearch(self, x):
        self.userSearch = x

    def parsingStock(self):
        #still need to output the found stock to the News Frame/Canvas
        filteredSearch = search[100]
        j = 0
        for i in self.userSearch:
            if(i == str.find("AUD") or i == str.find("CAD") or i == str.find("EUR") or i == str.find("USD") or i == str.find("NZD") or i == str.find("GBP")):
                print ("hello")
            else:
                print ("Hekki")

#method to output the search links to window                
def SearchResult(x, outputWindow):
    text = tk.Text(outputWindow, height = 3, width = 3)
    userInput = re.split(' |/', x.get())
    for i in userInput:
        if(i == "AUD" or i == "CAD" or i == "EUR" or i == "USD" or i == "NZD" or i == "GBP"):
            #userSearch = search(i, userInput)
            #ws.webParser(userSearch.getStockName())
            text.insert(tk.END, i)
    
    

    
    
    text.pack()
    text.config(state = "disabled")
def placeHolder():
    print ("Hello WOrlds")
#method that disables all quicksearches   
def disableCurrency(a,b,c,d,e,f,g):
    a.config(state = "disabled")
    b.config(state = "disabled")
    c.config(state = "disabled")
    d.config(state = "disabled")
    e.config(state = "disabled")
    f.config(state = "disabled")
    g.config(state = "disabled")
    a.deselect()
    b.deselect()
    c.deselect()
    d.deselect()
    e.deselect()
    f.deselect()
    g.deselect()
#method that shows and checks in the quicksearches
def ShowCurrency(a,b,c,d,e,f,g):
    a.config(state = "normal", command = lambda: placeHolder())
    b.config(state = "normal", command = lambda: placeHolder())
    c.config(state = "normal", command = lambda: placeHolder())
    d.config(state = "normal", command = lambda: placeHolder())
    e.config(state = "normal", command = lambda: placeHolder())
    f.config(state = "normal", command = lambda: placeHolder())
    g.config(state = "normal", command = lambda: placeHolder())
    a.select()
    b.select()
    c.select()
    d.select()
    e.select()
    f.select()
    g.select()

def Search(window):
    uSet = st.userSettings()
    var = tk.IntVar()
    #Search Bar which will take in user input
    searchFrame = tk.Frame(window)
    tk.Label(searchFrame).pack(side = tk.LEFT)
    edit = tk.Entry(searchFrame, width = int(.10 * uSet.getWidth()))
    edit.pack(side = tk.LEFT, fill = tk.BOTH, expand =1)
    edit.bind("<Return>", (lambda event: SearchResult(edit, OutputFrame)))
    edit.focus_set()
    searchButton = tk.Button(searchFrame, text = "Search", command = lambda: SearchResult(edit, OutputFrame))
    searchButton.pack(side = tk.RIGHT)

    searchFrame.pack(side = tk.TOP)

    #Checkboxes for quick searches for currencies such as AUD, USD
    searchBoxes = tk.Frame(window)
    
    AUD = tk.Checkbutton(searchBoxes, text = "AUD", bd = 4, command = lambda: placeHolder())
    AUD.pack(side = tk.LEFT)
    CAD = tk.Checkbutton(searchBoxes, text = "CAD", bd = 4, command = lambda: placeHolder())
    CAD.pack(side = tk.LEFT)
    EUR = tk.Checkbutton(searchBoxes, text = "EUR", bd = 4, command = lambda: placeHolder())
    EUR.pack(side = tk.LEFT)
    GBP = tk.Checkbutton(searchBoxes, text = "GBP", bd = 4,command =lambda: placeHolder())
    GBP.pack(side = tk.LEFT)
    NZD = tk.Checkbutton(searchBoxes, text = "NZD", bd = 4,command = lambda: placeHolder())
    NZD.pack(side = tk.LEFT)
    JPY = tk.Checkbutton(searchBoxes, text = "JPY", bd = 4, command = lambda: placeHolder())
    JPY.pack(side = tk.LEFT)
    USD = tk.Checkbutton(searchBoxes, text = "USD", bd = 4,command =lambda: placeHolder())
    USD.pack(side = tk.LEFT)
    CO = tk.Button(searchBoxes, text = "Currency Only", bd = 4, command =lambda: ShowCurrency(AUD,CAD,EUR,GBP,NZD,JPY,USD))
    CO.pack(side = tk.LEFT)
    SO = tk.Button(searchBoxes, text = "Stock Only", bd = 4, command =lambda: disableCurrency(AUD,CAD,EUR,GBP,NZD,JPY,USD))
    SO.pack(side = tk.LEFT)
    searchBoxes.pack(side = tk.TOP)
    #Setting the Stock Only button to disable 
    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    
    OutputFrame = tk.Frame(window, bg = "yellow", height = int(.25 * uSet.getHeight()), width = int(.75 * uSet.getWidth()))
    
    #OutputCanvas = tk.Canvas(OutputFrame, height = int(.25 * uSet.getHeight()), width = int(.75 * uSet.getWidth()))
    #OutputCanvas.pack()
    OutputFrame.pack()
   
