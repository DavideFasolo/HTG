import tkinter as tk
from tkinter import *
from tkinter.ttk import *
class PulsanteMenu:
    def __init__(self, container, workpath: str, png_image: str, comando='', stato:int=0):
        self.icona = tk.PhotoImage(file=workpath + 'icns\\' + png_image)
        self.pulsante = Button(container)
        self.pulsante.configure(text='apri vda', image=self.icona, command=comando)
        self.pulsante.pack(side=LEFT)
        if stato > 0:
            self.pulsante.configure(state=NORMAL)
        else:
            self.pulsante.configure(state=DISABLED)
