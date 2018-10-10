import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import os
import configparser
class Htg_gui:
    workpath=str(os.getcwd())+"\\Configurazione\\"
    Config = configparser.ConfigParser()
    Config.read(workpath+"config.kg")
    def __init__(proprio,genitore):
        #------------------------------------------------------
        butt_main_w=32
        butt_menu_w=24
        text_w=85
        butt_p=5
        butt_py="0.4m"
        icnsize_main=32
        icnsize_menu=24
        #------------------------------------------------------
        proprio.gen_1=genitore
        sezioni=proprio.Config.sections()
        lung_sez=len(sezioni)
        print('numero sezioni='+str(lung_sez)+':\n')
        print(sezioni)

        def set_box(sez,arg):
            print(sez+arg)
            def setta(sez,arg,val):
                proprio.Config[sez][arg]=val
                with open(proprio.workpath+"config.kg", 'w') as cfgfile:
                    proprio.Config.write(cfgfile)
            proprio.Config.read(proprio.workpath+"config.kg")
            print(proprio.Config.get(sez,arg))
            proprio.container1=Frame(genitore)
            proprio.container1.pack(fill=X)
            proprio.container1.configure(padding=butt_p)
            proprio.etk=Label(genitore, text=arg)
            proprio.etk.pack()
            proprio.valore=Entry(genitore)
            proprio.valore.insert(0,proprio.Config.get(sez,arg))
            proprio.sez=sez
            proprio.arg=arg
            proprio.valore.pack()
            def setta_f():
                proprio.val=str(proprio.valore.get())
                setta(proprio.sez,proprio.arg,proprio.val)
            proprio.butt_set=Button(proprio.container1)
            proprio.butt_set.configure(text='salva',
                                        command=setta_f)
            proprio.butt_set.pack()
            
        set_box('formattazione txt','etichette coordinate')
        set_box('formattazione txt','coordinate z')
        set_box('formattazione txt','intestazione')
                
impostazioni = Tk()
impostazioni.title("Impostazioni")
impostazioni.iconbitmap(Htg_gui.workpath+"\\icns\\conf.ico")
heg_gui=Htg_gui(impostazioni)
impostazioni.mainloop()
