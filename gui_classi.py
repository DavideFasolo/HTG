import tkinter as tk
from tkinter import *
from tkinter.ttk import *
class PulsanteMenu:
    def __init__(self, container, workpath: str, png_image: str, comando='', stato:int=1):
        self.icona = tk.PhotoImage(file=workpath + 'icns\\' + png_image)
        self.pulsante = tk.Button(container)
        self.pulsante.configure(text='apri vda', image=self.icona, takefocus=0,
                                bg='#2d2926', relief=FLAT, command=comando, highlightbackground='#423831',
                                highlightcolor='#423831', bd=0.5, highlightthickness=1,
                                activebackground='#423831', activeforeground='#423831')
        self.pulsante.pack(side=LEFT, padx=7)
        if stato > 0:
            self.pulsante.configure(state=NORMAL)
        else:
            self.pulsante.configure(state=DISABLED)
