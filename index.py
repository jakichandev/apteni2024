from tkinter import *
from tkinter import ttk
import json
from utils.constants import *
from utils.worksWithData import *
from model.aptene import Aptene

fileData = open('./data/apteni.json')
data = json.load(fileData)
fileData.close()
allApteni = list(data)

root = Tk()
root.title("Apteni 2024")
root.geometry("800x600")
root.minsize(500,300)
root.configure(background=TEXT_COLOR)

root.columnconfigure(0, weight=1),
root.columnconfigure(1, weight=1),
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

mainFrame = Frame(root, bg=TEXT_COLOR)
mainFrame.grid(row=0, column=0)
mainFrame.rowconfigure(0, weight=1)
mainFrame.rowconfigure(1, weight=1)
mainFrame.rowconfigure(2, weight=1)
mainFrame.rowconfigure(3, weight=1)

listFrame = Frame(root, bg=TEXT_COLOR)
listFrame.grid(row=0,column=1, rowspan=2, sticky='nsew')

welcomeLabel = Label(mainFrame, text="Apteni 2024\nper test", font="Helvetica, 25", bg=TEXT_COLOR, foreground="#fff").grid(row=0, column=0)

query = StringVar()
searchInput = Entry(mainFrame, background="#fff", foreground=TEXT_COLOR, border=0, textvariable=query)
searchInput.grid(row=1, column=0, pady=(10))

singleApteneFrame = Frame(root, bg="#fff")
singleApteneFrame.columnconfigure(0, weight=1)
singleApteneFrame.columnconfigure(1, weight=1)
singleApteneFrame.columnconfigure(2, weight=1)
singleApteneFrame.columnconfigure(3, weight=1)
singleApteneFrame.rowconfigure(0, weight=1)
singleApteneFrame.rowconfigure(1, weight=1)
singleApteneFrame.rowconfigure(2, weight=1)
singleApteneFrame.rowconfigure(3, weight=1)
singleApteneFrame.rowconfigure(4, weight=1)
singleApteneFrame.grid(row=0, column=2, sticky='nsew')

aptene = Aptene(singleApteneFrame)

aptene.createWidgets()
aptene.showInGUI()

submitSearch = Button(mainFrame, text="Cerca", highlightbackground="#fff", background=TEXT_COLOR)
submitSearch.grid(row=2, column=0)

msgBox = Label(mainFrame, foreground="#E60D0D", background='#fff')

submitSearch.bind('<Button-1>', lambda event: search(event, listFrame, allApteni, aptene, msgBox))


def search(event, listFrame, allApteni, apteneObj, msgWidget):
    
    filteredApteni = list()
    word = query.get()
    msg = StringVar()
    
    for aptene in allApteni:
        
        if word in aptene["title"] or word in aptene["title"].lower():
            print(word)
            print('true')
            filteredApteni.append(aptene)
  
    if (len(filteredApteni) > 0):
        msgWidget.grid_forget()
        print(len(filteredApteni))
        allApteni = filteredApteni
        renderList(listFrame, allApteni, apteneObj)
    else:
        msg.set('nessun risultato trovato!')
        msgWidget.config(text=msg.get())
        msgWidget.grid(row=3,column=0)


renderList(listFrame, allApteni, aptene)
print(allApteni)


root.mainloop()
