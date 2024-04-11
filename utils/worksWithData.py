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
            print(matchedAptene["cas"])
            aptene.configText(matchedAptene["id"], matchedAptene["title"], matchedAptene["description"], matchedAptene["pm"], matchedAptene["cas"], matchedAptene["category"], matchedAptene["cod-firm"], matchedAptene["formula"], matchedAptene["synonymus"])
            aptene.changeText()
        



def renderList(widget, data, aptene):
    
    #inserimento dati nella Listbox
    for item in data:
        widget.insert(END, item["title"])

    widget.pack(pady=5, padx=2, fill='both')
    
    #assegnamento funzione openSingle quando viene triggerato l'evento di selezione di un elemento della Listbox
    widget.bind('<<ListboxSelect>>', lambda cb: openSingle(cb, aptene))