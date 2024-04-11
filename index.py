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
root.geometry("800x800")
root.minsize(600, 600)

mainFrame = Frame(root, bg="#fff")
mainFrame.rowconfigure((0,1,2), weight=1)
mainFrame.columnconfigure((0,1,2), weight=1)
mainFrame.place(relx=0, y=0, relheight=1, relwidth=0.35)

listFrame = Frame(root, bg=BG_BASE)
listFrame.place(relx=0.35, rely=0, relwidth=0.2, relheight=1)

welcomeLabel = Label(mainFrame, text="Apteni 2024\nper test", font=('helvetica', 30, 'bold'), bg="#fff", foreground=TEXT_COLOR).grid(row=1, column=1, sticky=N)
query = StringVar()
searchInput = Entry(mainFrame, background="#fff", foreground=TEXT_COLOR, border=0, textvariable=query)
searchInput.grid(row=1, column=1, pady=10, sticky=S)
submitSearch = Button(mainFrame, text="Cerca", highlightbackground="#fff", background=TEXT_COLOR)
submitSearch.grid(row=2, column=1, sticky=N)

singleApteneParent = Frame(root, background=BG_BASE)
singleApteneParent.place(relx=0.55, rely=0, relwidth=0.45, relheight=1)

singleApteneFrame = Frame(singleApteneParent, bg=BG_BASE)
singleApteneFrame.place(x=0, y=0, relwidth=1, relheight=1)
singleApteneFrame.columnconfigure((0,1,2,3,4,5), weight=1)
singleApteneFrame.rowconfigure((0,1,2,4), weight=1)
singleApteneFrame.rowconfigure(3, weight=2)
aptene = Aptene(singleApteneFrame)
aptene.createWidgets()
aptene.showInGUI()
msgBox = Label(mainFrame, foreground="#E60D0D", background='#fff')
lab = Label(listFrame, text='lista completa', bg=BG_BASE, foreground=TEXT_COLOR).pack(fill="x")
listBox = Listbox(listFrame, background=BG_BASE, foreground="#fff", cursor="plus", selectbackground="#000", font=('helvetica', 12, 'bold'))
submitSearch.bind('<Button-1>', lambda event: search(event, listBox, allApteni, aptene, msgBox))


def search(event, widget, allApteni, apteneObj, msgWidget):
    widget.delete(0,END)
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
        renderList(widget, allApteni, apteneObj)
    else:
        msg.set('nessun risultato trovato!')
        msgWidget.config(text=msg.get())
        msgWidget.grid(row=2,column=1)
    

renderList(listBox, allApteni, aptene)
print(allApteni)


root.mainloop()
