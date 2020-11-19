import tkinter as tk
import WindowCommands.settings as st
import GUI.WebScraper as ws
import GUI.stockPrediction as sp
import re



#store the 60 days information to print
def graphOutput(x):
    file1 = open("SearchResults.txt","a")
    file1.write("\n" + x + "\n")
    file1.close()
    sp.createReport(x)
#sets the graph to output only the selected searck
def quickSearch(a, var):
    if(a.cget("text") == "AUD" and var.get() == 1):
        graphOutput(a.cget("text"))
       
    elif(a.cget("text") == "CAD" and var.get() == 1):
        graphOutput(a.cget("text"))
        
    elif(a.cget("text") == "EUR" and var.get() == 1):
        graphOutput(a.cget("text"))
        
    elif(a.cget("text") == "USD" and var.get() == 1):
        graphOutput(a.cget("text"))
        
    elif(a.cget("text") == "NZD" and var.get() == 1):
        graphOutput(a.cget("text"))
        
    elif(a.cget("text") == "GBP" and var.get() == 1):
        graphOutput(a.cget("text"))
       
    elif(a.cget("text") == "JPY" and var.get() ==  1):
        graphOutput(a.cget("text"))
       
    
#method to output the search links to window                
def SearchResult(input, outPut, scrollbar):
    userInput = re.split(" ", input.get())
    outPut.delete("1.0","end")
    outPut.update()
    ws.formatOutput(outPut, userInput, scrollbar)
    for i in userInput:
        if("AUD" in i or "CAD" in i or "EUR" in i or "USD" in i or "NZD" in i or "GBP" in i):
            j = re.split("[ |/]", i)
            for i in j:
                if("AUD" == i or "CAD" == i or "EUR" == i or "USD" == i or "NZD" == i or "GBP" == i):
                    #graphOutput(i)
                    print()
    outPut.pack()

#method that disables all quicksearches   
def disableCurrency(a,b,c,d,e,f,g):
    #grays out the button sand unchecks them
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
    #degrays all the checkbuttons
    a.config(state = "normal")
    b.config(state = "normal")
    c.config(state = "normal")
    d.config(state = "normal")
    e.config(state = "normal")
    f.config(state = "normal")
    g.config(state = "normal")
    #toggles button on provoke the command
    a.invoke()
    b.invoke()
    c.invoke()
    d.invoke()
    e.invoke()
    f.invoke()
    g.invoke()

def Search(window):
    uSet = st.userSettings()
    var = tk.IntVar()
    #Search Bar which will take in user input
    searchFrame = tk.Frame(window)
    tk.Label(searchFrame).pack(side = tk.LEFT)
    edit = tk.Entry(searchFrame, width = int(.10 * uSet.getWidth()))
    edit.pack(side = tk.LEFT, fill = tk.BOTH, expand =1)
    edit.bind("<Return>", (lambda event: SearchResult(edit, text, scrollbar)))
    edit.focus_set()
    searchButton = tk.Button(searchFrame, text = "Search", command = lambda: SearchResult(edit, text, scrollbar))
    searchButton.pack(side = tk.RIGHT)

    searchFrame.pack(side = tk.TOP)
    #Initialization of checkbox int variables
    searchBoxes = tk.Frame(window)
    varA = tk.IntVar()
    varC = tk.IntVar()
    varE = tk.IntVar()
    varG = tk.IntVar()
    varN = tk.IntVar()
    varJ = tk.IntVar()
    varU = tk.IntVar()

    #Checkboxes for quick searches for currencies such as AUD, USD
    CG = tk.Button(searchBoxes, text = "Clear Graph", bd = 4)
    CG.pack(side = tk.LEFT)
    AUD = tk.Checkbutton(searchBoxes, text = "AUD", bd = 4,variable = varA, command =lambda: quickSearch(AUD, varA))
    AUD.pack(side = tk.LEFT)
    CAD = tk.Checkbutton(searchBoxes, text = "CAD", bd = 4,variable = varC, command =lambda:  quickSearch(CAD, varC))
    CAD.pack(side = tk.LEFT)
    EUR = tk.Checkbutton(searchBoxes, text = "EUR", bd = 4,variable = varE, command =lambda:  quickSearch(EUR, varE))
    EUR.pack(side = tk.LEFT)
    GBP = tk.Checkbutton(searchBoxes, text = "GBP", bd = 4, variable = varG, command =lambda: quickSearch(GBP, varG))
    GBP.pack(side = tk.LEFT)
    NZD = tk.Checkbutton(searchBoxes, text = "NZD", bd = 4,variable = varN, command =lambda: quickSearch(NZD, varN))
    NZD.pack(side = tk.LEFT)
    JPY = tk.Checkbutton(searchBoxes, text = "JPY", bd = 4, variable = varJ, command =lambda:  quickSearch(JPY, varJ))
    JPY.pack(side = tk.LEFT)
    USD = tk.Checkbutton(searchBoxes, text = "USD", bd = 4,variable = varU, command =lambda: quickSearch(USD, varU))
    USD.pack(side = tk.LEFT)
    CO = tk.Button(searchBoxes, text = "Currency Only", bd = 4, command =lambda: ShowCurrency(AUD,CAD,EUR,GBP,NZD,JPY,USD))
    CO.pack(side = tk.LEFT)
    SO = tk.Button(searchBoxes, text = "Stock Only", bd = 4, command =lambda: disableCurrency(AUD,CAD,EUR,GBP,NZD,JPY,USD))
    SO.pack(side = tk.LEFT)
    searchBoxes.pack(side = tk.TOP)

    #Scroll bar for output
    scrollbar = tk.Scrollbar(window)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    #Output    
    OutputFrame = tk.Frame(window, bg = "white", height = int(.15 * uSet.getHeight()), width = int(.50 * uSet.getWidth()))
    OutputFrame.grid_propagate(False)
    OutputFrame.pack()
    text = tk.Text(OutputFrame, height = int(.25 * uSet.getHeight()), width = int(.09 * uSet.getWidth()))
