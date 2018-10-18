from aprifiles import *
from creamatrix import *
from infrastructure import InterfaceConfiguration
from outcsv import *
from outcnc import *
from outdxf import *
from settings import *
from gui_classi import *

######################################################################
from settings import Htg_dxfset

root = tk.Tk()
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width * 0.5, height * 0.5, width * 0.1, height * 0.1))
image_file = 'Configurazione\\assets\\KG-Splash.png'
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height * 0.5, width=width * 0.5, bg="black")
canvas.create_image(width * 0.5 / 2, height * 0.5 / 2, image=image)
canvas.pack()
root.after(4000, root.destroy)
root.mainloop()


class HtgGui:
    workpath = str(os.getcwd()) + "\\Configurazione\\"
    cf = InterfaceConfiguration(workpath)

    def __init__(self, genitore):
        larghezza_testo_principale = 85
        padding_pulsanti = 5

        self.gen_1 = genitore

        self.area_menu = Frame(genitore)
        self.area_menu.pack(fill=X)
        self.area_menu.configure(padding=padding_pulsanti)

        self.testo_output = Frame(genitore)
        self.testo_output.pack(fill=X)
        self.testo_output.configure(padding=padding_pulsanti)

        self.info_comandi = Frame(genitore)
        self.info_comandi.pack(side=TOP, expand=1, fill=tk.BOTH)
        self.info_comandi.configure(padding=padding_pulsanti)

        self.butt_opn = PulsanteMenu(self.area_menu, self.workpath, 'file-opn.png', self.apri_file, 1)
        self.butt_csv = PulsanteMenu(self.area_menu, self.workpath, 'file-csv.png')
        self.butt_dxf = PulsanteMenu(self.area_menu, self.workpath, 'file-dxf.png')
        self.butt_txt = PulsanteMenu(self.area_menu, self.workpath, 'file-txt.png')
        self.butt_cnc = PulsanteMenu(self.area_menu, self.workpath, 'file-cnc.png')

        self.mw = Text(self.testo_output, height=1)
        self.mw.tag_configure('normale', foreground='#476042', font=('Tempus Sans ITC', 8))
        self.mw.tag_configure('csv', foreground='green', font=('Tempus Sans ITC', 8))
        self.mw.tag_configure('dxf', foreground='crimson', font=('Tempus Sans ITC', 8))
        self.mw.tag_configure('cnc', foreground='indigo', font=('Tempus Sans ITC', 8))
        self.mw.tag_configure('txt', foreground='mediumblue', font=('Tempus Sans ITC', 8))
        self.mw.insert(END, 'selezionare un file vda', 'normale')
        self.mw.config(relief=FLAT, bg='#E1E1E1', state=DISABLED)
        self.mw.pack(side=LEFT, expand=1, fill=tk.X)

        self.S = Scrollbar(self.info_comandi)
        self.S.pack(side=RIGHT, fill=Y)
        self.T = Text(self.info_comandi, height=20, width=larghezza_testo_principale)
        self.T.pack(side=TOP, expand=1, fill=tk.BOTH)
        self.S.config(command=self.T.yview)
        self.T.config(wrap=NONE, relief=FLAT)
        self.T.insert(END, "per cominciare, seleziona un file vda usando il pulsante apposito\n")
        self.T.config(state=DISABLED)
        self.T['yscrollcommand'] = self.S.set

    def apri_file(self):
        t = aprivda()
        if t:
            self.p = t.p
            self.f = t.f
            self.in_file = t.in_file
            self.processa_file()
        else:
            self.T.config(state=NORMAL)
            self.T.replace(1.0,END,'File non trovato\n\nPer favore ritenta')
            self.T.config(state=DISABLED)
            self.butt_csv.pulsante.configure(state=DISABLED)
            self.butt_dxf.pulsante.configure(state=DISABLED)
            self.butt_txt.pulsante.configure(state=DISABLED)
            self.butt_cnc.pulsante.configure(state=DISABLED)

    def processa_file(self):
        self.fori = leggivda(self.in_file, self.cf.arrot)
        self.T.config(state=NORMAL)
        self.T.delete(1.0, END)
        i = 0
        texfori = '\nFile vda processato\n'
        texfori += "Rilevati e memorizzati i seguenti fori nell'ordine:\n\n"
        texfori += 'Pos\t\tDiam\t\tX\t\tY\t\tZ\n'
        while i < len(self.fori):
            texfori += str(i + 1) + '\t\t'
            texfori += str(self.fori[i][0]) + '\t\t'
            texfori += str(self.fori[i][1]) + '\t\t'
            texfori += str(self.fori[i][2]) + '\t\t'
            texfori += str(self.fori[i][3]) + '\n'
            i += 1

        self.T.insert(END, texfori)
        self.T.config(state=DISABLED)
        self.mw.config(state=NORMAL)
        self.mw.delete(1.0, END)
        self.mw.insert(END, 'File vda importato correttamente', 'normale')
        self.mw.config(state=DISABLED, fg='#000000')
        print("file processato")

        def esportcsv():
            esporta_csv(self.fori, self.f, self.cf.separ, self.cf.virgo)
            self.mw.config(state=NORMAL)
            self.mw.delete(1.0, END)
            self.mw.insert(END, 'Esportazione file csv excel completata', 'csv')
            self.mw.config(state=DISABLED, bg='honeydew')

        def esportdxf():
            esporta_dxf(self.fori, self.f, self.workpath)
            self.mw.config(state=NORMAL)
            self.mw.delete(1.0, END)
            self.mw.insert(END, 'Esportazione file dxf R12 completata', 'dxf')
            self.mw.config(state=DISABLED, bg='mistyrose')

        def esportcnc():
            esporta_cnc(self.fori, self.p, self.f, self.workpath, self.cf.traduttore)
            self.mw.config(state=NORMAL)
            self.mw.delete(1.0, END)
            self.mw.insert(END, 'Esportazione file cnc completata', 'cnc')
            self.mw.config(state=DISABLED, bg='lavender')

        def esporttxt():
            esporta_txt(self.fori, self.p, self.f, self.workpath)
            self.mw.config(state=NORMAL)
            self.mw.delete(1.0, END)
            self.mw.insert(END, 'Esportazione file txt completata', 'txt')
            self.mw.config(state=DISABLED, bg='lightcyan')

        self.butt_csv.pulsante.configure(state=NORMAL, command=esportcsv)
        self.butt_dxf.pulsante.configure(state=NORMAL, command=esportdxf)
        self.butt_cnc.pulsante.configure(state=NORMAL, command=esportcnc)
        self.butt_txt.pulsante.configure(state=NORMAL, command=esporttxt)


def esciii():
    radice.destroy()


def imposta_txt():
    impostazioni_txt_window = Toplevel()
    impostazioni_txt_window.title("Impostazioni file di testo")
    impostazioni_txt_window.iconbitmap(Htg_txtset.workpath + "\\icns\\conf.ico")
    set_txt = Htg_txtset(impostazioni_txt_window)
    impostazioni_txt_window.mainloop()


def imposta_csv():
    impostazioni_csv_window = Toplevel()
    impostazioni_csv_window.title("Impostazioni file csv")
    impostazioni_csv_window.iconbitmap(Htg_csvset.workpath + "\\icns\\conf.ico")
    set_csv_gui = Htg_csvset(impostazioni_csv_window)
    impostazioni_csv_window.mainloop()


def imposta_dxf():
    impostazioni_dxf_window = Toplevel()
    impostazioni_dxf_window.title("Impostazioni dxf")
    impostazioni_dxf_window.iconbitmap(Htg_dxfset.workpath + "\\icns\\conf.ico")
    set_dxf_gui = Htg_dxfset(impostazioni_dxf_window)
    impostazioni_dxf_window.mainloop()


radice = Tk()
radice.title("Hole Table Generator by Kill Goliath")
radice.iconbitmap(HtgGui.workpath + "\\icns\\icona.ico")
heg_gui = HtgGui(radice)
butt_sett = Menu(radice)
impostazioni = Menu(butt_sett, tearoff=0)
impostazioni.add_command(label="file di testo", command=imposta_txt)
impostazioni.add_command(label="file csv", command=imposta_csv)
impostazioni.add_command(label="file dxf", command=imposta_dxf)
butt_sett.add_cascade(label="Impostazioni", menu=impostazioni)
butt_sett.add_command(label='esci', command=esciii)
radice.config(menu=butt_sett)
radice.mainloop()
