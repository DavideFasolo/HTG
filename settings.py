import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import os
import configparser
class Htg_txtset:
    workpath=str(os.getcwd())+"\\Configurazione\\"
    Config = configparser.ConfigParser()
    Config.read(workpath+"config.kg")
    def __init__(proprio,genitore):
        proprio.gen_1=genitore
        def make_box(ccc,sez):
            ccc=LabelFrame(genitore,
                           borderwidth='1m',
                           text=sez)
            ccc.pack(fill=X, side=TOP)
            ccc.configure(padding=0)
            ddd=Frame(ccc)
            ddd.pack(fill=Y)
            ddd.configure(padding=0)
            proprio.Config.read(proprio.workpath+"config.kg")
            opt_mat=list()
            val_mat=list()
            for key in proprio.Config[sez]:
                opt_mat.append(key)
            i=0
            while i<len(opt_mat):
                proprio.contn=Frame(ddd)
                proprio.contn.pack(fill=X, side=LEFT)
                proprio.contn.configure(padding=1)
                if (proprio.Config.get(sez,opt_mat[i])=='si' or proprio.Config.get(sez,opt_mat[i])=='no'):
                    val_mat.append(StringVar())
                    proprio.cbox = ttk.Checkbutton(ddd,
                                    variable=val_mat[i],
                                    offvalue='no',
                                    onvalue='si',
                                    text=opt_mat[i])
                    val_mat[i].set(proprio.Config.get(sez,opt_mat[i]))
                    proprio.cbox.pack(side=LEFT)
                else:
                    proprio.etk=Label(proprio.contn, text=opt_mat[i])
                    proprio.etk.pack()
                    val_mat.append(StringVar())
                    proprio.valore=Entry(proprio.contn,
                                         textvariable=val_mat[i])
                    val_mat[i].set(proprio.Config.get(sez,opt_mat[i]))
                    proprio.valore.pack()
                i+=1
            def set_val():
                i=0
                while i<len(opt_mat):
                    proprio.Config.set(sez,opt_mat[i],val_mat[i].get())
                    i+=1
                with open(proprio.workpath+"config.kg", 'w') as configfile:
                    proprio.Config.write(configfile)
            proprio.butt_set=Button(ccc)
            proprio.butt_set.configure(text='salva',
                                       command=set_val)
            proprio.butt_set.pack(side=BOTTOM)
        ###################################################################
        make_box('proprio.cont1','formattazione txt')

class Htg_csvset:
    workpath=str(os.getcwd())+"\\Configurazione\\"
    Config = configparser.ConfigParser()
    Config.read(workpath+"config.kg")
    def __init__(proprio,genitore):
        proprio.gen_1=genitore
        def make_box(ccc,sez):
            ccc=LabelFrame(genitore,
                           borderwidth='1m',
                           text=sez)
            ccc.pack(fill=X, side=TOP)
            ccc.configure(padding=0)
            ddd=Frame(ccc)
            ddd.pack(fill=Y)
            ddd.configure(padding=0)
            proprio.Config.read(proprio.workpath+"config.kg")
            opt_mat=list()
            val_mat=list()
            for key in proprio.Config[sez]:
                opt_mat.append(key)
            i=0
            while i<len(opt_mat):
                proprio.contn=Frame(ddd)
                proprio.contn.pack(fill=X, side=LEFT)
                proprio.contn.configure(padding=1)
                if (proprio.Config.get(sez,opt_mat[i])=='si' or proprio.Config.get(sez,opt_mat[i])=='no'):
                    val_mat.append(StringVar())
                    proprio.cbox = ttk.Checkbutton(ddd,
                                    variable=val_mat[i],
                                    offvalue='no',
                                    onvalue='si',
                                    text=opt_mat[i])
                    val_mat[i].set(proprio.Config.get(sez,opt_mat[i]))
                    proprio.cbox.pack(side=LEFT)
                else:
                    proprio.etk=Label(proprio.contn, text=opt_mat[i])
                    proprio.etk.pack()
                    val_mat.append(StringVar())
                    proprio.valore=Entry(proprio.contn,
                                         textvariable=val_mat[i])
                    val_mat[i].set(proprio.Config.get(sez,opt_mat[i]))
                    proprio.valore.pack()
                i+=1
            def set_val():
                i=0
                while i<len(opt_mat):
                    proprio.Config.set(sez,opt_mat[i],val_mat[i].get())
                    i+=1
                with open(proprio.workpath+"config.kg", 'w') as configfile:
                    proprio.Config.write(configfile)
            proprio.butt_set=Button(ccc)
            proprio.butt_set.configure(text='salva',
                                       command=set_val)
            proprio.butt_set.pack(side=BOTTOM)
        ###################################################################
        make_box('proprio.cont1','formattazione csv')



class Htg_dxfset:
    workpath=str(os.getcwd())+"\\Configurazione\\"
    Config = configparser.ConfigParser()
    Config.read(workpath+"config.kg")
    colorfile=open(workpath+'coloridxf.kg','r')
    colorread=colorfile.readlines()
    colorfile.close()
    colormatrix=list()
    i=0
    while i<len(colorread):
        colormatrix.append(colorread[i].split(','))
        colormatrix[i][0]=int(colormatrix[i][0])
        colormatrix[i][1]=int(colormatrix[i][1])
        colormatrix[i][2]=int(colormatrix[i][2])
        colormatrix[i]='#%02x%02x%02x' % (colormatrix[i][0],colormatrix[i][1],colormatrix[i][2])
        i+=1
    def __init__(proprio,genitore):
        proprio.gen_1=genitore
        def make_box(ccc,sez):
            ccc=ttk.LabelFrame(genitore,
                           borderwidth='3m',
                           text=sez)
            ccc.pack(fill=Y, side=LEFT)
            ccc.configure(padding=5)
            ddd=Frame(ccc)
            ddd.pack(fill=X)
            ddd.configure(padding=0)
            proprio.Config.read(proprio.workpath+"config.kg")
            opt_mat=list()
            val_mat=list()
            def colcho(proprio,i):
                colorchoose=Toplevel()
                def setcolor(g):
                    colvar=proprio.colormatrix[g]
                    val_mat[i].set(g)
                    colorchoose.destroy()
                g=0
                h=0
                f=0
                while g<len(proprio.colormatrix):
                    cbut=tk.Button(colorchoose,
                                   width=2,
                                   height=1,
                                   relief=FLAT,
                                   overrelief=RIDGE,
                                   command=lambda g=g: setcolor(g),
                                   bg=proprio.colormatrix[g])
                    cbut.grid(row=f,column=h)
                    if h==19:
                        h=-1
                        f+=1
                    h+=1
                    g+=1
            for key in proprio.Config[sez]:
                opt_mat.append(key)
            i=0
            while i<len(opt_mat):
                proprio.contn=Frame(ddd)
                proprio.contn.pack(fill=X, side=TOP)
                if (proprio.Config.get(sez,opt_mat[i])=='si' or proprio.Config.get(sez,opt_mat[i])=='no'):
                    val_mat.append(StringVar())
                    proprio.cbox = ttk.Checkbutton(ddd,
                                    variable=val_mat[i],
                                    offvalue='no',
                                    onvalue='si',
                                    text=opt_mat[i])
                    val_mat[i].set(proprio.Config.get(sez,opt_mat[i]))
                    proprio.cbox.pack(side=TOP)
                else:
                    if opt_mat[i].find('colore')!=-1:
                        proprio.etk=Label(proprio.contn, text=opt_mat[i])
                        proprio.etk.pack()
                        val_mat.append(StringVar())
                        val_mat[i].set(int(proprio.Config.get(sez,opt_mat[i])))
                        cch=Button(ddd,
                                      textvariable=val_mat[i],
                                   command=lambda i=i: colcho(proprio,i))
                        cch.pack(side=TOP, fill=X)
                    else:
                        proprio.etk=Label(proprio.contn, text=opt_mat[i])
                        proprio.etk.pack()
                        val_mat.append(StringVar())
                        proprio.valore=Entry(proprio.contn,
                                             textvariable=val_mat[i])
                        val_mat[i].set(proprio.Config.get(sez,opt_mat[i]))
                        proprio.valore.pack(side=TOP, fill=X)
                sep_m=ttk.Separator(ddd, orient="horizontal")
                sep_m.pack(expand=2,fill=X, pady=8)
                i+=1
            def set_val():
                i=0
                while i<len(opt_mat):
                    proprio.Config.set(sez,opt_mat[i],val_mat[i].get())
                    i+=1
                with open(proprio.workpath+"config.kg", 'w') as configfile:
                    proprio.Config.write(configfile)
            proprio.butt_set=Button(ccc)
            proprio.butt_set.configure(text='salva',
                                       command=set_val)
            proprio.butt_set.pack(side=BOTTOM, fill=X)
        ###################################################################
        make_box('proprio.cont1','stile cerchi')
        make_box('proprio.cont1','stile assi')
        make_box('proprio.cont1','stile etichette')


#impostazioni = Tk()
#impostazioni.title("Impostazioni dxf")
#impostazioni.iconbitmap(Htg_dxfset.workpath+"\\icns\\conf.ico")
#set_dxf_gui=Htg_dxfset(impostazioni)
#impostazioni.mainloop()
