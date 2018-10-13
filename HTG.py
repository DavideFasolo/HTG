import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from aprifiles import *
from creamatrix import *
from outcsv import *
from outcnc import *
from outdxf import *
from settings import *
import configparser
######################################################################
root = tk.Tk()
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.5, height*0.5, width*0.1, height*0.1))
image_file = 'Configurazione\\assets\\KG-Splash.png'
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.5, width=width*0.5, bg="black")
canvas.create_image(width*0.5/2, height*0.5/2, image=image)
canvas.pack()
root.after(5000, root.destroy)
root.mainloop()
class Htg_gui:
    #aggiunta rilevazione directory di lavoro
    workpath=str(os.getcwd())+"\\Configurazione\\"
    Config = configparser.ConfigParser()
    Config.read(workpath+"config.kg")
    arrot=int(Config.get('ambiente','cifre decimali delle coordinate'))
    traduttore=str(Config.get('postprocessore cnc','nome postprocessore'))
    separ=Config.get('formattazione csv','separatore colonne')
    virgo=Config.get('formattazione csv','virgola')
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
        proprio.icn_apri=tk.PhotoImage(file=proprio.workpath+
                               "icns\\folder-orange-open.png")
        proprio.icn_csv=tk.PhotoImage(file=proprio.workpath+
                               "icns\\csv-file.png")
        proprio.icn_dxf=tk.PhotoImage(file=proprio.workpath+
                               "icns\\file-dxf.png")
        proprio.icn_cnc=tk.PhotoImage(file=proprio.workpath+
                               "icns\\file-cnc.png")
        proprio.icn_txt=tk.PhotoImage(file=proprio.workpath+
                               "icns\\file-txt.png")
        stile = ttk.Style()
        stile.configure("TButton", foreground="black",
                        height=32,
                        width=32)

        proprio.gen_1=genitore
        proprio.container1=Frame(genitore)
        proprio.container1.pack(fill=X)
        proprio.container1.configure(padding=butt_p)

        proprio.msgwrite=Frame(genitore)
        proprio.msgwrite.pack(fill=X)
        proprio.msgwrite.configure(padding=butt_p)

        proprio.container3=Frame(genitore)
        proprio.container3.pack(fill=X)
        proprio.container3.configure(padding=butt_p)

        proprio.butt_apri=Button(proprio.container1)
        proprio.butt_apri.configure(text='apri vda',
                                    image=proprio.icn_apri,
                                    width=butt_main_w,
                                    style='TButton',
                                    command=proprio.aprifile)
        proprio.butt_apri.pack(side=LEFT)

        proprio.butt_csv=Button(proprio.container1)
        proprio.butt_csv.configure(text='salva csv',
                                   image=proprio.icn_csv)
        proprio.butt_csv.pack(side=LEFT)
        proprio.butt_csv.configure(state=DISABLED)

        proprio.butt_dxf=Button(proprio.container1)
        proprio.butt_dxf.configure(text='salva dxf',
                                   image=proprio.icn_dxf)
        proprio.butt_dxf.pack(side=LEFT)
        proprio.butt_dxf.configure(state=DISABLED)

        proprio.butt_cnc=Button(proprio.container1)
        proprio.butt_cnc.configure(text='salva cnc',
                                   image=proprio.icn_cnc)
        proprio.butt_cnc.pack(side=LEFT)
        proprio.butt_cnc.configure(state=DISABLED)

        proprio.butt_txt=Button(proprio.container1)
        proprio.butt_txt.configure(text='salva txt',
                                   image=proprio.icn_txt)
        proprio.butt_txt.pack(side=LEFT)
        proprio.butt_txt.configure(state=DISABLED)

        proprio.container2=Frame(genitore)
        proprio.container2.pack(side=TOP,expand=1,fill=tk.BOTH)
        proprio.container2.configure(padding=butt_p)

        proprio.mw = Text(proprio.msgwrite, height=1)
        proprio.mw.tag_configure('normale', foreground='#476042',
						font=('Tempus Sans ITC', 8))
        proprio.mw.tag_configure('csv',
                                 foreground='green',
                                 font=('Tempus Sans ITC', 8))
        proprio.mw.tag_configure('dxf',
                                 foreground='crimson',
                                 font=('Tempus Sans ITC', 8))
        proprio.mw.tag_configure('cnc',
                                 foreground='indigo',
                                 font=('Tempus Sans ITC', 8))
        proprio.mw.tag_configure('txt',
                                 foreground='mediumblue',
                                 font=('Tempus Sans ITC', 8))


        proprio.mw.insert(END, 'selezionare un file vda','normale')

        proprio.mw.config(relief=FLAT,
                          bg='#E1E1E1',
                          state=DISABLED)
        proprio.mw.pack(side=LEFT,expand=1,fill=tk.X)

        proprio.S = Scrollbar(proprio.container2)
        proprio.S.pack(side=RIGHT, fill=Y)
        proprio.T = Text(proprio.container2, height=20, width=text_w)
        proprio.T.pack(side=TOP,expand=1,fill=tk.BOTH)
        proprio.S.config(command=proprio.T.yview)
        proprio.T.config(wrap=NONE,
                         relief=FLAT)
        proprio.T.insert(END, "per cominciare, seleziona un file vda usando il pulsante apposito\n")
        proprio.T.config(state=DISABLED)
        proprio.T['yscrollcommand'] = proprio.S.set
        
    def aprifile(proprio):
        t=aprivda()
        if t:
            proprio.p=t.p
            proprio.f=t.f
            proprio.in_file=t.in_file
            print('\nTrovato il file\n')
            print(proprio.f)
            print('\nnella cartella\n')
            print(proprio.f)
            proprio.processafile()
        else:
            print('\nNessun file selezionato\n')
            proprio.butt_csv.configure(state=DISABLED)
    def giaprocessato(proprio):
        print('il file è già stato processato, selezionane uno nuovo, esci o esporta')
    def processafile(proprio):
        proprio.fori=leggivda(proprio.in_file,proprio.arrot)
        proprio.T.config(state=NORMAL)
        proprio.T.delete(1.0,END)
        i=0
        texfori=str('Pos\t\tDiam\t\tX\t\tY\t\tZ\n')
        while i<len(proprio.fori):
            texfori+=str(i+1)+'\t\t'
            texfori+=str(proprio.fori[i][0])+'\t\t'
            texfori+=str(proprio.fori[i][1])+'\t\t'
            texfori+=str(proprio.fori[i][2])+'\t\t'
            texfori+=str(proprio.fori[i][3])+'\n'
            i+=1
        proprio.T.insert(END, texfori)
        proprio.T.config(state=DISABLED)
        proprio.mw.config(state=NORMAL)
        proprio.mw.delete(1.0,END)
        proprio.mw.insert(END, 'File vda importato correttamente','normale')
        proprio.mw.config(state=DISABLED,
                              fg='#000000')
        print("file processato")
        def esportcsv():
            esporta_csv(proprio.fori,proprio.f,proprio.separ,proprio.virgo)
            proprio.mw.config(state=NORMAL)
            proprio.mw.delete(1.0,END)
            proprio.mw.insert(END, 'Esportazione file csv excel completata','csv')
            proprio.mw.config(state=DISABLED,
                              bg='honeydew')
        def esportdxf():
            esporta_dxf(proprio.fori, proprio.f, proprio.workpath)
            proprio.mw.config(state=NORMAL)
            proprio.mw.delete(1.0,END)
            proprio.mw.insert(END, 'Esportazione file dxf R12 completata','dxf')
            proprio.mw.config(state=DISABLED,
                              bg='mistyrose')
        def esportcnc():
            esporta_cnc(proprio.fori,proprio.p,proprio.f,proprio.workpath,proprio.traduttore)
            proprio.mw.config(state=NORMAL)
            proprio.mw.delete(1.0,END)
            proprio.mw.insert(END, 'Esportazione file cnc completata','cnc')
            proprio.mw.config(state=DISABLED,
                              bg='lavender')
        def esporttxt():
            esporta_txt(proprio.fori,proprio.p,proprio.f,proprio.workpath)
            proprio.mw.config(state=NORMAL)
            proprio.mw.delete(1.0,END)
            proprio.mw.insert(END, 'Esportazione file txt completata','txt')
            proprio.mw.config(state=DISABLED,
                              bg='lightcyan')
        proprio.butt_csv.configure(state=NORMAL,
                                   command=esportcsv)
        proprio.butt_dxf.configure(state=NORMAL,
                                   command=esportdxf)
        proprio.butt_cnc.configure(state=NORMAL,
                                   command=esportcnc)
        proprio.butt_txt.configure(state=NORMAL,
                                   command=esporttxt)

def esciii():
    radice.destroy()
def sett_1():
    impostazioni = Toplevel()
    impostazioni.title("Impostazioni file di testo")
    impostazioni.iconbitmap(Htg_txtset.workpath+"\\icns\\conf.ico")
    set_txt=Htg_txtset(impostazioni)
    impostazioni.mainloop()
def sett_2():
    impostazioni = Toplevel()
    impostazioni.title("Impostazioni file csv")
    impostazioni.iconbitmap(Htg_csvset.workpath+"\\icns\\conf.ico")
    set_csv_gui=Htg_csvset(impostazioni)
    impostazioni.mainloop()
def sett_3():
    impostazioni = Toplevel()
    impostazioni.title("Impostazioni dxf")
    impostazioni.iconbitmap(Htg_dxfset.workpath+"\\icns\\conf.ico")
    set_dxf_gui=Htg_dxfset(impostazioni)
    impostazioni.mainloop()
radice = Tk()
radice.title("Hole Table Generator by Kill Goliath")
radice.iconbitmap(Htg_gui.workpath+"\\icns\\icona.ico")
heg_gui=Htg_gui(radice)
butt_sett=Menu(radice)
impostazioni=Menu(butt_sett,tearoff=0)
impostazioni.add_command(label="file di testo",
                              command=sett_1)
impostazioni.add_command(label="file csv",
                              command=sett_2)
impostazioni.add_command(label="file dxf",
                              command=sett_3)
butt_sett.add_cascade(label="Impostazioni", menu=impostazioni)
butt_sett.add_command(label='esci',
                      command=esciii)
radice.config(menu=butt_sett)
radice.mainloop()
