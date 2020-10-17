import tkinter as tk

class search(object):
    def __init__(self, stockName, userSearch):
        self.stockName = stockName
        self.userSearch = userSearch

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
        for i in self.userSearch:
            if(i == str.find("AUD") or i == str.find("CAD") or i == str.find("EUR") or i == str.find("USD") or i == str.find("NZD") or i == str.find("GBP")):
                return 1
            else:
                return 0



def Search(window):
    #Takes in user input and includes searchbar
    print("hello")