import tkinter as tk
from tkinter import *
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer


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


FR_PRIVATE = 0x10
FR_NOT_ENUM = 0x20


def loadfont(fontpath, private=True, enumerable=False):
    if isinstance(fontpath, bytes):
        pathbuf = create_string_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExA
    elif isinstance(fontpath, str):
        pathbuf = create_unicode_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
    else:
        raise TypeError('fontpath must be of type str or unicode')

    flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
    numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
    return bool(numFontsAdded)