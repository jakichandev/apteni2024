from tkinter import *
from utils.constants import *
import json


def openSingle(event, aptene):

    #inizializzazione aptene cliccato su valore None
    matchedAptene = None
    
    #ottenimento valore selezionato
    selected = event.widget.get(ANCHOR)

    #apertura file apteni.json e ottenimento dati ricevuti da esso nella variabile apteniJson
    filedata = open('./data/apteni.json')
    apteniJson = json.load(filedata)
    filedata.close()
    
   #ciclo for sull'array degli oggetti derivanti da apteniJson 
    for item in apteniJson:
        #se il valore ciclato corrisponde a selected assegna matchedAptene all'oggetto corrisposto
        if item["title"] == selected:
            matchedAptene = item
            aptene.configText(matchedAptene["id"], matchedAptene["title"], matchedAptene["description"])
            print(aptene.id)
            aptene.changeText()
        



def renderList(parent, data, aptene):
    listBox = Listbox(parent, background="#3aafff", foreground=TEXT_COLOR, cursor="plus", selectbackground="#e8e8e8", font="helvetica,18")
    
    #inserimento dati nella Listbox
    for item in data:
        listBox.insert(END, item["title"])

    listBox.grid(row=0, column=0, pady=10)
    
    #assegnamento funzione openSingle quando viene triggerato l'evento di selezione di un elemento della Listbox
    listBox.bind('<<ListboxSelect>>', lambda cb: openSingle(cb, aptene))