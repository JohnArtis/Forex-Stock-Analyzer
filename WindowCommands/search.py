import tkinter as tk
import WindowCommands.settings as st
class search(object):
    def __init__(self, stockName, userSearch):
        self.stockName = stockName
        self.userSearch = userSearch
        searchArray = search[1000]

    def getStockName(self):
        return self.__stockName

    def getUserSearch(self):
        return self.__userSearch

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
            



def Search(window):
    uSet = st.userSettings()

    #Search Bar which will take in user input
    searchFrame = tk.Frame(window)
    tk.Label(searchFrame).pack(side = tk.LEFT)
    edit = tk.Entry(searchFrame, width = int(.10 * uSet.getWidth()))
    edit.pack(side = tk.LEFT, fill = tk.BOTH, expand =1)
    edit.focus_set()
    searchButton = tk.Button(searchFrame, text = "Search",  )
    searchButton.pack(side = tk.RIGHT)

    searchFrame.pack(side = tk.TOP)

    #Checkboxes for quick searches such as AUD, USD, AAPL
    searchBoxes = tk.Frame(window)
    AUD = tk.Checkbutton(searchBoxes, text = "AUD", bd = 4, width = 5)
    AUD.pack(side = tk.LEFT)
    CAD = tk.Checkbutton(searchBoxes, text = "CAD", bd = 4, width = 5)
    CAD.pack(side = tk.LEFT)
    EUR = tk.Checkbutton(searchBoxes, text = "EUR", bd = 4, width = 5)
    EUR.pack(side = tk.LEFT)
    GBP = tk.Checkbutton(searchBoxes, text = "GBP", bd = 4, width = 5)
    GBP.pack(side = tk.LEFT)
    NZD = tk.Checkbutton(searchBoxes, text = "NZD", bd = 4, width = 5)
    NZD.pack(side = tk.LEFT)
    JPY = tk.Checkbutton(searchBoxes, text = "JPY", bd = 4, width = 5)
    JPY.pack(side = tk.LEFT)
    USD = tk.Checkbutton(searchBoxes, text = "USD", bd = 4, width = 5)
    USD.pack(side = tk.LEFT)
    
    searchBoxes.pack(side = tk.TOP)

    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    OutputFrame = tk.Frame(window, bg = "yellow", height = int(.25 * uSet.getHeight()), width = int(.75 * uSet.getWidth()))
    
    OutputFrame.pack()
   