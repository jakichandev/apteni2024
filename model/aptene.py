from tkinter import *
from utils.constants import *

class Aptene():

    id_widget = None
    title_widget = None
    description_widget = None
    
    def __init__(self, id, title, description, parent):
        self.id = id
        self.title = title,
        self.description = description
        self.parent = parent
    
    def __setId(self):
        self.id_widget = Label(self.parent, text=self.id, foreground="#fff", background=TEXT_COLOR)

    def __setTitle(self):
        self.title_widget = Label(self.parent, text=self.title, foreground="#fff", background=TEXT_COLOR)

    def __setDescription(self):
        self.description_widget = Message(self.parent, text=self.description, foreground="#fff", background=TEXT_COLOR)

    def createWidgets(self):
        self.__setId()
        self.__setTitle()
        self.__setDescription()

    def showInGUI(self):
        self.id_widget.grid(row=0, column=1)
        self.title_widget.grid(row=1, column=1)
        self.description_widget.grid(row=2, column=1)

    def configText(self, id, title, desc):
        self.id = id
        self.title = title
        self.description = desc

    def changeText(self):
        self.id_widget.config(text=self.id)
        self.title_widget.config(text=self.title)
        self.description_widget.config(text=self.description)