import configparser

from etik import *
from KG_dxf import *


class DrawingExchangeFormatConfigurations:
    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path + "config.kg")

        self.coord_z=config.get('ambiente','esporta coordinate Z dei cerchi')
        self.cer_livello=str(config.get('stile cerchi','livello'))
        self.cer_colore=str(config.get('stile cerchi','colore del tratto'))
        self.ass_colore=str(config.get('stile assi','colore tratto'))
        self.htesto=str(config.get('stile etichette','altezza caratteri'))
        self.tes_livello=str(config.get('stile etichette','livello testo'))
        self.tes_colore=str(config.get('stile etichette','colore testo'))
        self.angolo=float(config.get('stile etichette','angolazione'))
        self.etk_livello=config.get('stile etichette','livello')
        self.etk_colore=str(config.get('stile etichette','colore tratto'))
        self.etk_dmodA=float(config.get('avanzate','scala dimensioni testo due cifre'))
        self.etk_dmodB=float(config.get('avanzate','scala dimensioni testo una cifra'))
        self.etk_dmodAx=float(config.get('avanzate','fattore offset tag due cifre x'))
        self.etk_dmodAy=float(config.get('avanzate','fattore offset tag due cifre y'))
        self.etk_dmodBx=float(config.get('avanzate','fattore offset tag una cifra x'))
        self.etk_dmodBy=float(config.get('avanzate','fattore offset tag una cifra y'))


def esporta_dxf(fori,f, workpath):
    cf = DrawingExchangeFormatConfigurations(workpath)

    cdf=f+"dxf"
    out_dxf=open(cdf,"w+")
    out_dxf.write('999\nFile "'+cdf+'" esportato tramite "Hole Table Generator" by "Kill Goliath"\n')
    out_dxf.write('999\nPowered by Davide Fasolo 2018\n')
    out_dxf.write('0\nSECTION\n')
    out_dxf.write('2\nENTITIES\n')

    i=0
    while i<len(fori):
        cr=fori[i][0]/2
        cx=fori[i][1]
        cy=fori[i][2]
        if cf.coord_z:
            cz=fori[i][3]
        else:
            cz=0
        i+=1
        out_dxf.write(dxf_cerchio(cx,cy,cz,cr, cf.cer_livello, cf.cer_colore))
        out_dxf.write(dxf_testo(coord_testo_etichetta(cx,cy,cz,cr, cf.htesto, cf.angolo,'x',i, cf.etk_dmodA, cf.etk_dmodB, cf.etk_dmodAx, cf.etk_dmodBx),coord_testo_etichetta(cx,cy,cz,cr, cf.htesto, cf.angolo,'y',i, cf.etk_dmodA, cf.etk_dmodB, cf.etk_dmodAy, cf.etk_dmodBy,),cz,0,0,str(i), cf.htesto, cf.tes_livello, cf.tes_colore))
        out_dxf.write(dis_etichetta(cx,cy,cz,cr, cf.htesto, cf.angolo, cf.etk_livello,i, cf.etk_colore, cf.etk_dmodA, cf.etk_dmodB))
    ###assi
    g=0
    maxx=fori[g][1]
    maxy=fori[g][2]
    minx=fori[g][1]
    miny=fori[g][2]
    while g<=len(fori)-1:
        if (fori[g][1]>maxx):
                maxx=fori[g][1]
        if (fori[g][2]>maxy):
                maxy=fori[g][2]
        if (fori[g][1]<minx):
                minx=fori[g][1]
        if (fori[g][2]<miny):
                miny=fori[g][2]
        g+=1
    if miny>0:
        miny=0
    out_dxf.write(dxf_linea(minx,0,0,maxx,0,0, cf.cer_livello, cf.ass_colore))
    out_dxf.write(dxf_linea(0,maxy,0,0,miny,0, cf.cer_livello, cf.ass_colore))
    #######
    out_dxf.write('0\nENDSEC\n0\nEOF')
    out_dxf.close()
    print("Creato il file \n"+cdf+"\n"+"Nella cartella dove si trova il file vda selezionato")
