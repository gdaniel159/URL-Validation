# Clase de la aplicacion, donde se alojaran las caracteristicas de la ventana

from tkinter import *

class App(Tk):

    def __init__(self):
        super().__init__()
        # Configure the root window
        # self.geometry("400x300")
        self.resizable(False,False)