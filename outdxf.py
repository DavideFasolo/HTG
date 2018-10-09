import configparser
from etik import *
from KG_dxf import *
def esporta_dxf(fori,f):

    workpath="C:\\Program Files (x86)\\Hole Table Generator\\Configurazione\\"
    Config = configparser.ConfigParser()
    Config.read(workpath+"config.kg")

    coord_z=str(Config.get('ambiente','esporta coordinate Z dei cerchi'))
    cer_livello=str(Config.get('stile cerchi','livello'))
    cer_colore=str(Config.get('stile cerchi','colore del tratto'))
    cer_spessore=str(Config.get('stile cerchi','spessore tratto'))
    ass_colore=str(Config.get('stile assi','colore tratto'))
    ass_spessore=str(Config.get('stile assi','spessore tratto'))
    htesto=str(Config.get('stile etichette','altezza caratteri'))
    tes_livello=str(Config.get('stile etichette','livello testo'))
    tes_colore=str(Config.get('stile etichette','colore testo'))
    angolo=float(Config.get('stile etichette','angolazione'))
    etk_livello=Config.get('stile etichette','livello')
    etk_colore=str(Config.get('stile etichette','colore tratto'))
    etk_dmodA=float(Config.get('avanzate','scala dimensioni testo due cifre'))
    etk_dmodB=float(Config.get('avanzate','scala dimensioni testo una cifra'))
    etk_dmodAx=float(Config.get('avanzate','fattore offset tag due cifre x'))
    etk_dmodAy=float(Config.get('avanzate','fattore offset tag due cifre y'))
    etk_dmodBx=float(Config.get('avanzate','fattore offset tag una cifra x'))
    etk_dmodBy=float(Config.get('avanzate','fattore offset tag una cifra y'))


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
        if coord_z:
            cz=fori[i][3]
        else:
            cz=0
        i+=1
        out_dxf.write(dxf_cerchio(cx,cy,cz,cr,cer_livello,cer_colore,cer_spessore))
        out_dxf.write(dxf_testo(coord_testo_etichetta(cx,cy,cz,cr,htesto,angolo,'x',i,etk_dmodA,etk_dmodB,etk_dmodAx,etk_dmodBx),coord_testo_etichetta(cx,cy,cz,cr,htesto,angolo,'y',i,etk_dmodA,etk_dmodB,etk_dmodAy,etk_dmodBy,),cz,0,0,str(i),htesto,tes_livello,tes_colore))
        out_dxf.write(dis_etichetta(cx,cy,cz,cr,htesto,angolo,etk_livello,i,etk_colore,etk_dmodA,etk_dmodB))
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
    out_dxf.write(dxf_linea(minx,0,0,maxx,0,0,cer_livello,ass_colore,ass_spessore))
    out_dxf.write(dxf_linea(0,maxy,0,0,miny,0,cer_livello,ass_colore,ass_spessore))
    #######
    out_dxf.write('0\nENDSEC\n0\nEOF')
    out_dxf.close()
    print("Creato il file \n"+cdf+"\n"+"Nella cartella dove si trova il file vda selezionato")
