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
    searchFrame = tk.Frame(window)
    tk.Label(searchFrame, text = "Search: ").pack(side = tk.LEFT)
    edit = tk.Entry(searchFrame)
    edit.pack(side = tk.LEFT, fill = tk.BOTH, expand =1)
    edit.focus_set()

    searchButton = tk.Button(searchFrame, text = "Find",  )
    searchButton.pack(side = tk.RIGHT)
    searchFrame.pack(side = tk.TOP)
