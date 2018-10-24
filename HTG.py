from aprifiles import *
from creamatrix import *
from KG_dxf import *
from infrastructure import InterfaceConfiguration
from infrastructure import DrawingExchangeFormatConfigurations
from outcsv import *
from outcnc import *
from settings import *
from gui_classi import *
from settings import Htg_dxfset
from tkinter.ttk import *

######################################################################

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
root.after(400, root.destroy)
root.mainloop()

workpath = str(os.getcwd()) + "\\Configurazione\\"
loadfont(workpath + 'assets\\RENT_0.ttf')
loadfont(workpath + 'assets\\erbos_draco_1st_open_nbp.ttf')


class HtgGui:
    workpath = str(os.getcwd()) + "\\Configurazione\\"
    cf = InterfaceConfiguration(workpath)
    cfdxf = DrawingExchangeFormatConfigurations(workpath)

    def __init__(self, genitore):
        # variabili grafiche
        self.canv_bool = 0
        larghezza_testo_principale = 6
        altezza_testo_principale = 2
        padding_pulsanti = 8
        gui_style = ttk.Style()
        gui_style.configure('My.TButton', foreground='#2d2926')
        gui_style.configure('My.TFrame', background='#2d2926')
        # variabili grafiche

        self.gen_1 = genitore

        self.area_operativa = tk.Frame(genitore,  bg='#2d2926')
        self.area_operativa.pack(side=LEFT, expand=0, fill=BOTH)
        self.area_operativa.configure(width=radice.winfo_screenwidth()/7,
                                      height=radice.winfo_screenheight()/1.2,
                                    bd=0, highlightbackground='#423831',
                                    highlightthickness=1)

        self.area_disegno = tk.Frame(genitore, bg='#2d2926')
        self.area_disegno.pack(expand=0, fill=BOTH)
        self.area_disegno.configure(width=radice.winfo_screenwidth()/2.5,
                                      height=radice.winfo_screenheight()/1.2,
                                    bd=0, highlightbackground='#423831',
                                    highlightthickness=1)

        self.area_menu = Frame(self.area_operativa)
        self.area_menu.pack(expand=0, fill=X)
        self.area_menu.configure(width=radice.winfo_screenwidth()/7,padding=padding_pulsanti, style='My.TFrame')

        self.testo_output = Frame(self.area_operativa)
        self.testo_output.pack(expand=0, fill=X)
        self.testo_output.configure(padding=padding_pulsanti, style='My.TFrame')

        self.info_comandi = Frame(self.area_operativa)
        self.info_comandi.pack(side=TOP, expand=1, fill=BOTH)
        self.info_comandi.configure(padding=padding_pulsanti, style='My.TFrame')

        self.butt_opn = PulsanteMenu(self.area_menu, self.workpath, 'file-opn.png', self.apri_file, 1)
        self.butt_csv = PulsanteMenu(self.area_menu, self.workpath, 'file-csv.png')
        self.butt_dxf = PulsanteMenu(self.area_menu, self.workpath, 'file-dxf.png')
        self.butt_txt = PulsanteMenu(self.area_menu, self.workpath, 'file-txt.png')
        self.butt_cnc = PulsanteMenu(self.area_menu, self.workpath, 'file-cnc.png')

        self.mw = Text(self.testo_output, height=1)
        self.mw.tag_configure('normale', foreground='white', font=('Erbos Draco 1st Open NBP', 10))
        self.mw.tag_configure('csv', foreground='green', font=('Erbos Draco 1st Open NBP', 10))
        self.mw.tag_configure('dxf', foreground='crimson', font=('Erbos Draco 1st Open NBP', 10))
        self.mw.tag_configure('cnc', foreground='indigo', font=('Erbos Draco 1st Open NBP', 10))
        self.mw.tag_configure('txt', foreground='mediumblue', font=('Erbos Draco 1st Open NBP', 10))
        self.mw.insert(END, 'selezionare un file vda', 'normale')
        self.mw.config(relief=FLAT, bg='#423d39', state=DISABLED)
        self.mw.pack(side=LEFT, expand=1)

        self.T = Text(self.info_comandi, height=altezza_testo_principale, width=larghezza_testo_principale)
        self.T.tag_configure('normale', foreground='white', font=('Erbos Draco 1st Open NBP', 10))
        self.T.pack(side=TOP, expand=1, fill=tk.BOTH)
        self.T.config(wrap=NONE, relief=FLAT, font=('Roentgen NBP', 11), background='#2d2926', foreground='white')
        self.T.insert(END, "per cominciare, seleziona un file vda\nusando il pulsante apposito\n")
        self.T.config(state=DISABLED)

    def apri_file(self):
        t = aprivda(apri_file_diag())
        if t:
            self.p = t.p
            self.f = t.f
            self.in_file = t.in_file
            self.processa_file()
        else:
            # reimposta tutto
            self.T.config(state=NORMAL)
            self.T.replace(1.0,END,'File non trovato\n\nPer favore ritenta')
            self.T.config(state=DISABLED)
            self.mw.config(state=NORMAL)
            self.mw.delete(1.0, END)
            self.mw.insert(END, 'selezionare un file vda', 'normale')
            self.mw.config(relief=FLAT, bg='#423d39', state=DISABLED)
            if self.canv_bool:
                self.disegno.destroy()
            # reimposta tutto

    def processa_file(self):
        self.fori = leggivda(self.in_file, self.cf.arrot)
        self.T.config(state=NORMAL)
        self.T.delete(1.0, END)
        i = 0
        v = 0
        self.min_x = self.fori[i][1] - self.fori[i][0] / 2
        self.max_x = self.fori[i][1] + self.fori[i][0] / 2
        self.min_y = self.fori[i][2] - self.fori[i][0] / 2
        self.max_y = self.fori[i][2] + self.fori[i][0] / 2
        self.fori_obj = list()
        self.fori_stesso_diam = list()
        while i < len(self.fori):
            cr = self.fori[i][0] / 2
            cx = self.fori[i][1]
            cy = self.fori[i][2]
            if self.cfdxf.coord_z:
                cz = self.fori[i][3]
            else:
                cz = 0

            if cx - cr < self.min_x:
                self.min_x = cx - cr
            if cx + cr > self.max_x:
                self.max_x = cx + cr
            if cy - cr < self.min_y:
                self.min_y = cy - cr
            if cy + cr > self.max_y:
                self.max_y = cy + cr

            foro000 = Forotag(cx, cy, cz, cr, self.cfdxf.htesto, self.cfdxf.angolo, i + 1, 4, self.cfdxf.cer_colore,
                              self.cfdxf.cer_livello, self.cfdxf.etk_colore, self.cfdxf.etk_livello,
                              self.cfdxf.tes_livello, self.cfdxf.tes_colore)

            cr *= 2
            if i == 0:
                self.fori_stesso_diam.append(foro000)
                self.fori_obj.append([cr, self.fori_stesso_diam])
            else:
                if cr != self.fori_obj[v][0]:
                    self.fori_stesso_diam = [foro000]
                    self.fori_obj.append([cr, self.fori_stesso_diam])
                    v += 1
                else:
                    if cr == self.fori_obj[v][0]:
                        self.fori_obj[v][1].append(foro000)
            i += 1
        texfori = 'Trovati i seguenti ' + str(len(self.fori)) + ' fori:\n\n'
        i = 0
        q = 1
        while i < len(self.fori_obj):
            texfori += 'N. ' + str(len(self.fori_obj[i][1])) + ' fori di diametro ' +\
                       str(self.fori_obj[i][0]) + ' mm:\n'
            u = 0
            while u < len(self.fori_obj[i][1]):
                texfori += str(q) + ':\t' + 'x ' + str(self.fori_obj[i][1][u].centro.x)
                texfori += '\t\ty ' + str(self.fori_obj[i][1][u].centro.y)
                texfori += '\t\tz ' + str(self.fori_obj[i][1][u].centro.z) + '\n'
                q += 1
                u += 1
            texfori += '\n'
            i += 1
        self.asse_x = Linea(self.min_x, 0, self.max_x, 0, self.cfdxf.cer_livello, self.cfdxf.ass_colore)
        self.asse_y = Linea(0, self.max_y, 0, self.min_y, self.cfdxf.cer_livello, self.cfdxf.ass_colore)
        i = 0
########################################################################################################################
#   Disegno
########################################################################################################################
        self.canv_pad = 50
        self.canv_height = self.area_operativa.winfo_height()
        self.canv_y = (self.max_y - self.min_y) + self.canv_pad * 2
        self.canv_x = (self.max_x - self.min_x) + self.canv_pad * 2
        self.canv_scale = self.canv_y / self.canv_height
        self.canv_width = self.canv_x / self.canv_scale
        if self.canv_bool:
            self.disegno.destroy()
        self.disegno = tk.Canvas(master=self.area_disegno,
                              width=self.canv_width, height=self.canv_height,
                              bg='#2d2926', bd=0, relief=FLAT, highlightthickness=0, takefocus=0)
        self.canv_bool = 1
        in_colore = open(self.workpath + 'coloridxf.kg', 'r')
        in_colore.seek(0, 0)
        mm = int(self.cfdxf.cer_colore)
        while mm > 0:
            col_cer = in_colore.readline().split(',')
            mm -= 1
        self.colore_cerchi = '#%02x%02x%02x' % (int(col_cer[0]), int(col_cer[1]), int(col_cer[2]))
        in_colore.close()
        while i < len(self.fori_obj):
            u = 0
            while u < len(self.fori_obj[i][1]):
                oval_x1 = self.fori_obj[i][1][u].centro.x - self.fori_obj[i][1][u].cerchio.raggio - self.min_x \
                          + self.canv_pad
                oval_y1 = self.max_y - self.fori_obj[i][1][u].centro.y - self.fori_obj[i][1][u].cerchio.raggio \
                          + self.canv_pad
                oval_x2 = self.fori_obj[i][1][u].centro.x + self.fori_obj[i][1][u].cerchio.raggio - self.min_x \
                          + self.canv_pad
                oval_y2 = self.max_y - self.fori_obj[i][1][u].centro.y + self.fori_obj[i][1][u].cerchio.raggio \
                          + self.canv_pad
                self.disegno.create_oval(oval_x1 / self.canv_scale,
                                         oval_y1 / self.canv_scale,
                                         oval_x2 / self.canv_scale,
                                         oval_y2 / self.canv_scale,
                                         outline=self.colore_cerchi,
                                         width=1.5)
                u += 1
            i += 1
        self.disegno.create_line(self.canv_pad / self.canv_scale,
                                 (self.max_y + self.canv_pad) / self.canv_scale,
                                 (self.max_x - self.min_x + self.canv_pad) / self.canv_scale,
                                 (self.max_y + self.canv_pad) / self.canv_scale,
                                 dash=(7, 1, 2, 1),
                                 fill='red')
        self.disegno.create_line((self.canv_pad - self.min_x) / self.canv_scale,
                                 self.canv_pad / self.canv_scale,
                                 (self.canv_pad - self.min_x) / self.canv_scale,
                                 (self.max_y - self.min_y + self.canv_pad) / self.canv_scale,
                                 dash=(7, 1, 2, 1),
                                 fill='red')
        self.disegno.pack(expand=YES, fill=BOTH, side=RIGHT)
########################################################################################################################
#   Fine Disegno
########################################################################################################################
        self.T.insert(END, texfori)
        self.T.config(state=DISABLED)
        self.mw.config(state=NORMAL)
        self.mw.delete(1.0, END)
        self.mw.insert(END, 'File vda importato correttamente', 'normale')
        self.mw.config(state=DISABLED, fg='#000000')

        def esportcsv():
            esporta_csv(self.fori, self.f, self.cf.separ, self.cf.virgo)
            self.mw.config(state=NORMAL)
            self.mw.delete(1.0, END)
            self.mw.insert(END, 'Esportazione file csv excel completata', 'csv')
            self.mw.config(state=DISABLED, bg='honeydew')

        def esportdxf():
            cdf = self.f + "dxf"
            intestazione = DxfFormat(cdf)
            out_dxf = open(cdf, "w+")
            out_dxf.write(intestazione.dxf_start)
            out_dxf.write(self.asse_x.dxfcode)
            out_dxf.write(self.asse_y.dxfcode)
            i = 0
            while i < len(self.fori_obj):
                u = 0
                while u < len(self.fori_obj[i][1]):
                    out_dxf.write(self.fori_obj[i][1][u].dxfcode)
                    u += 1
                i += 1
            out_dxf.write(intestazione.dxf_end)
            out_dxf.close()
            
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
wid = int(radice.winfo_screenwidth()/8)
hei = int(radice.winfo_screenheight() / 20)
radice.geometry('+%d+%d' % (wid, hei))
radice.title("Hole Table Generator by Kill Goliath")
radice.iconbitmap(HtgGui.workpath + "\\icns\\icona.ico")
heg_gui = HtgGui(radice)
butt_sett = Menu(radice)
impostazioni = Menu(butt_sett, tearoff=0)
impostazioni.add_command(label="File txt", command=imposta_txt)
impostazioni.add_command(label="File csv", command=imposta_csv)
impostazioni.add_command(label="File dxf", command=imposta_dxf)
butt_sett.add_cascade(label="Impostazioni", menu=impostazioni)
butt_sett.add_command(label='Esci', command=esciii)
radice.config(menu=butt_sett, bg='#2d2926')
radice.mainloop()
