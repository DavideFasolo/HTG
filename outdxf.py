from etik import *
from KG_dxf import *
from infrastructure import DrawingExchangeFormatConfigurations


def esporta_dxf(fori, f, workpath):
    cf = DrawingExchangeFormatConfigurations(workpath)
    cdf = f + "dxf"
    out_dxf = open(cdf, "w+")
    out_dxf.write('999\nFile "' + cdf + '" esportato tramite "Hole Table Generator" by "Kill Goliath"\n')
    out_dxf.write('999\nPowered by Davide Fasolo 2018\n')
    out_dxf.write('0\nSECTION\n')
    out_dxf.write('2\nENTITIES\n')
    i = 0
    minx=fori[i][1]-fori[i][0]/2
    maxx = fori[i][1] + fori[i][0] / 2
    miny = fori[i][2] - fori[i][0] / 2
    maxy = fori[i][2] + fori[i][0] / 2
    while i < len(fori):
        cr = fori[i][0] / 2
        cx = fori[i][1]
        cy = fori[i][2]
        if cf.coord_z:
            cz = fori[i][3]
        else:
            cz = 0
        i += 1
        if cx-cr<minx:
            minx=cx-cr
        if cx+cr>maxx:
            maxx=cx+cr
        if cy-cr<miny:
            miny=cy-cr
        if cy+cr>maxy:
            maxy=cy+cr
        foro1=Forotag(cx,cy,cz,cr,cf.htesto,cf.angolo,i,4,cf.cer_colore,cf.cer_livello,
                      cf.etk_colore,cf.etk_livello,cf.tes_livello,cf.tes_colore)
        exec('foro%d = Forotag(%f,%f,%f,%f,%f,%f,%d,4,%s,"%s",%s,"%s","%s",%s)' % (i,cx,cy,cz,cr,
                                                                                      cf.htesto,cf.angolo,i,
                                                                                      cf.cer_colore,cf.cer_livello,
                                                                                      cf.etk_colore,cf.etk_livello,
                                                                                      cf.tes_livello,cf.tes_colore))
        exec("out_dxf.write(foro%d.dxfcode)" % i)
        out_dxf.write(
            dis_etichetta(cx, cy, cz, cr, cf.htesto, cf.angolo, cf.etk_livello, i, cf.etk_colore, cf.etk_dmodA,
                          cf.etk_dmodB))

    assex = linea(minx, 0, maxx, 0, cf.cer_livello, cf.ass_colore)
    assey = linea(0, maxy, 0, miny, cf.cer_livello, cf.ass_colore)
    out_dxf.write(assex.dxfcode)
    out_dxf.write(assey.dxfcode)
    #######
    out_dxf.write('0\nENDSEC\n0\nEOF')
    out_dxf.close()
    print("Creato il file \n" + cdf + "\n" + "Nella cartella dove si trova il file vda selezionato")
