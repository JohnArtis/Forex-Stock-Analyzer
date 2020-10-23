import requests
from bs4 import BeautifulSoup
from lxml import html
import json
import tkinter as tk
from collections import OrderedDict
import re
import WindowCommands.settings as st
import csv



def webParser(x):
    
    URL = 'https://search.yahoo.com/'

    values = {x : "currencies"}
    #url = 'https://finance.yahoo.com/' + str(x) + "&sort=active"    
    #req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})    
    #html = urlopen(req)
    data = parse.urlencode(values)
    data = data.encode('utf-8') # data should be bytes
    req = request.Request(URL, data)
    resp = request.urlopen(req)
    respData = resp.read()
    print(respData)

def newsParser(x):
    url = 'https://finance.yahoo.com'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find_all('a')
    tempList = []
    tempDict = {}
    for i in title:
        #0 Currencies
        if(i.text == "Currencies" and x == 0): 
            currency = url + i.get("href")
            page2 = requests.get(currency)
            soup = BeautifulSoup(page2.content, 'html.parser')
            stock = soup.find_all("a")
            for i in stock:
                if(("AUD" in i.get("href") or "CAD" in i.get("href") or "EUR" in i.get("href") or "USD" in i.get("href") or "NZD" in i.get("href") or "GBP" in i.get("href")) and "quote" in i.get("href")):
                    currency = url + i.get("href")
                    page3 = requests.get(currency)
                    soup = BeautifulSoup(page3.content, 'html.parser')
                    j = re.split("[(]", soup.title.text)
                    openNumber = [i.get_text(separator=u' ') for i in soup.find_all("td")]
                    tempDict = {
                        "title" : j[0],
                        "href":  currency,
                        "Open": openNumber[3],
                        "Previous Close": openNumber[1],
                        "Current Day" : openNumber[7]
                    }
                    tempList.append(tempDict)
            return tempList     
        #1 is for stocks
        if(i.text == "Stocks: Most Actives" and x == 1):
            stocks = url + i.get("href")
            page2 = requests.get(stocks)
            soup = BeautifulSoup(page2.content, 'html.parser')
            stock = soup.find_all("a")
            for i in stock:
                if("quote" in i.get("href")):
                    stockLink = url+ i.get("href")
                    page3 = requests.get(stockLink)
                    soup = BeautifulSoup(page3.content, 'html.parser')
                    j = re.split("[)]", soup.title.text)
                    openNumber = [i.get_text(separator=u' ') for i in soup.find_all("td")]
                    tempDict = {
                        "title" :  j[0]+")",
                        "href":  stockLink,
                        "Open": openNumber[3],
                        "Previous Price": openNumber[1],
                        "Day Range" : openNumber[9]
                    }
                    tempList.append(tempDict)
            for i in range(3):
                tempList.pop(0)
            return tempList
                
                
def outPut(window, x):  
    uSet = st.userSettings()
    text = tk.Text(window, height = 25, width = 60)
    outList = newsParser(x)
    
    if(x == 1):
        text.insert(tk.CURRENT,("{:<10} {:<10} {:<10} {:<10}".format('Stock  |', 'Open   |', 'Previous Price  |', 'Day Range' + '\n')))
        
        [text.insert(tk.CURRENT,("{:<10} {:<5} {:<5} {:<10}".format(item['title'],item['Open'],item['Previous Price'],item['Day Range'] + '\n'))) for item in outList]
        text.pack()
    if(x == 0):
        text.insert(tk.CURRENT,("{:<10} {:<10} {:<10} {:<10}".format('Currency  |', 'Open  |', 'Previous Close  |', 'Current Day' + '\n')))
        text.insert(tk.CURRENT,("{:<10}{:<10}{:<10}{:<10}").format('----------|','-------|----','---------------|','------------'+"\n"))
        [text.insert(tk.CURRENT,("{:<10} {:<10} {:<10} {:<10}".format(item['title']+"  |",item['Open']+"  |",item['Previous Close']+"  |",item['Current Day'] + '\n'))) for item in outList]
        text.pack()
    
        

def test(window):
    text = tk.Text(window)
    text.insert(tk.END,"Hello")
    text.pack()
