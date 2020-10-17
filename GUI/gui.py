import tkinter as tk
import WindowCommands.menu as mn
import WindowCommands.news as nw
import WindowCommands.settings as st



#def Graph(self, graph):
    #show current Market and show a projected output



def gui():
    uSet = st.userSettings()
    
    #creates the main window for the GUI
    window = tk.Tk()
    canvas = tk.Canvas(window, height = uSet.getHeight(), width = uSet.getWidth())
    mn.Menu(window)
    nw.News(window)
    canvas.pack()
    window.mainloop()