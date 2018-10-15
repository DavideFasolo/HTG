from etik import *
from KG_dxf import *
from infrastructure import DrawingExchangeFormatConfigurations


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
        # cerchio1=cerchio(cx, cy, cz, cr, cf.cer_livello, cf.cer_colore)
        # out_dxf.write(cerchio1.dxfcode)
        exec('cerchio%d = cerchio(%f,%f,%f,%f,"%s","%s")' % (i, cx, cy, cz, cr, cf.cer_livello, cf.cer_colore))
        exec ("out_dxf.write(cerchio%d.dxfcode)" % i)
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
    assex=linea(minx,0,maxx,0, cf.cer_livello, cf.ass_colore)
    assey=linea(0,maxy,0,miny, cf.cer_livello, cf.ass_colore)
    out_dxf.write(assex.dxfcode)
    out_dxf.write(assey.dxfcode)
    #######
    out_dxf.write('0\nENDSEC\n0\nEOF')
    out_dxf.close()
    print("Creato il file \n"+cdf+"\n"+"Nella cartella dove si trova il file vda selezionato")
