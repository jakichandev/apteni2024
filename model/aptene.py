from tkinter import *
from utils.constants import *

class Aptene():
    
    id_widget = None
    title_widget = None
    description_widget = None
    alias_widget = None,
    pm_widget = None,
    cas_widget = None,
    category_widget = None
    cod_firma_widget = None
    formula_widget = None
    notes_widget = None
    synon_widget = None
    
    #Construttore con valori inizializzati di default a None
    def __init__(self, parent, id=None, title=None, description=None, alias=None, pm=None, cas=None, category=None, cod_firma=None, formula=None, synon=None, notes=None):
        
        self.id = id
        self.title = title,
        self.description = description
        self.alias = alias
        self.pm = pm
        self.cas = cas
        self.category = category
        self.cod_firma = cod_firma
        self.formula = formula
        self.notes = notes
        self.synon = synon
        self.parent = parent
    
    #Funzioni private setters per configurare i Widget da mostrare(inizializzati con campi vuoti)
    
    def __setId(self):
        self.id_widget = Label(self.parent, text=self.id, foreground="#fff", background=TEXT_COLOR)

    def __setTitle(self):
        self.title_widget = Label(self.parent, text="", foreground="#fff", background=TEXT_COLOR, font=('Helvetica', 18, 'bold'))

    def __setDescription(self):
        self.description_widget = Label(self.parent, text=self.description, foreground="#fff", background=TEXT_COLOR)

    def __setAlias(self):
        self.alias_widget = Label(self.parent, text=self.alias, foreground="#fff", background=TEXT_COLOR)
    
    def __setPm(self):
        self.pm_widget = Label(self.parent, text="PM\n", foreground="#fff", background=TEXT_COLOR)

    def __setCas(self):
        self.cas_widget = Label(self.parent, text="CAS\n", foreground="#fff", background=TEXT_COLOR)

    def __setCategory(self):
        self.category_widget = Label(self.parent, text='Categoria\n', foreground="#fff", background=TEXT_COLOR)

    def __setCodFirma(self):
        self.cod_firma_widget = Label(self.parent, text="Cod. FIRMA\n", foreground="#fff", background=TEXT_COLOR)

    def __setFormula(self):
        self.formula_widget = Label(self.parent, text="Formula\n", foreground="#fff", background=TEXT_COLOR, width=10, height=5)

    def __setSynon(self):
        self.synon_widget = Label(self.parent, text="Sinonimi: ", foreground="#fff", background=TEXT_COLOR)  

    #Funzione pubblica per eseguire i vari setters e creare i Widget
    
    def createWidgets(self):
        self.__setId()
        self.__setTitle()
        self.__setDescription()
        self.__setAlias()
        self.__setPm()
        self.__setCas()
        self.__setCategory()
        self.__setCodFirma()
        self.__setFormula()
        self.__setSynon()

    #Funzione pubblica per mostrare i widget
    
    def showInGUI(self):
        self.title_widget.grid(row=0, column=0, columnspan=3, sticky=NW)
        self.description_widget.grid(row=3, column=0, pady=10)
        self.pm_widget.grid(row=1, column=0, sticky=W, pady=10)
        self.cas_widget.grid(row=1, column=1, pady=10),
        self.category_widget.grid(row=1, column=2, pady=10),
        self.cod_firma_widget.grid(row=1, column=3, sticky=E, pady=10)
        self.formula_widget.grid(row=2, column=0)
        self.synon_widget.grid(row=4, column=0)

    #Funzione pubblica per modificare il contenuto degli attributi
    
    def configText(self, id, title, desc, pm, cas, category, cod_firma, formula, synon):
        self.id = id
        self.title = title
        self.description = desc
        self.pm = pm
        self.cas = cas
        self.category = category
        self.cod_firma = cod_firma
        self.formula = formula
        self.synon = synon

    #Funzione pubblica per configurare il contenuto degli attributi sul widget stesso
    
    def changeText(self):
        self.id_widget.config(text=self.id)
        self.title_widget.config(text=self.title)
        self.description_widget.config(text=self.description)
        self.pm_widget.config(text="PM\n" + self.pm)
        self.cas_widget.config(text="CAS\n" + self.cas)
        self.category_widget.config(text='Categoria\n' + self.category)
        self.cod_firma_widget.config(text="Cod. FIRMA\n" + self.cod_firma)
        self.formula_widget.config(text="Formula\n" + self.formula)
        self.synon_widget.config(text="Sinonimi:" + self.synon)