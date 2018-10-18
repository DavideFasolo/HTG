from KG_dxf import *
from infrastructure import DrawingExchangeFormatConfigurations


def esporta_dxf(fori, f, workpath):
    cf = DrawingExchangeFormatConfigurations(workpath)
    cdf = f + "dxf"
    intestazione=DxfFormat(cdf)
    out_dxf = open(cdf, "w+")
    out_dxf.write(intestazione.dxf_start)
    i = 0
    min_x = fori[i][1] - fori[i][0] / 2
    max_x = fori[i][1] + fori[i][0] / 2
    min_y = fori[i][2] - fori[i][0] / 2
    max_y = fori[i][2] + fori[i][0] / 2
    fori_obj = list()
    while i < len(fori):
        cr = fori[i][0] / 2
        cx = fori[i][1]
        cy = fori[i][2]
        if cf.coord_z:
            cz = fori[i][3]
        else:
            cz = 0
        i += 1
        if cx - cr < min_x:
            min_x = cx - cr
        if cx + cr > max_x:
            max_x = cx + cr
        if cy - cr < min_y:
            min_y = cy - cr
        if cy + cr > max_y:
            max_y = cy + cr

        foro000 = Forotag(cx, cy, cz, cr, cf.htesto, cf.angolo, i, 4, cf.cer_colore, cf.cer_livello, cf.etk_colore,
                          cf.etk_livello, cf.tes_livello, cf.tes_colore)
        out_dxf.write(foro000.dxfcode)
        fori_obj.append(foro000)

    asse_x = Linea(min_x, 0, max_x, 0, cf.cer_livello, cf.ass_colore)
    asse_y = Linea(0, max_y, 0, min_y, cf.cer_livello, cf.ass_colore)
    out_dxf.write(asse_x.dxfcode)
    out_dxf.write(asse_y.dxfcode)
    #######
    out_dxf.write(intestazione.dxf_end)
    out_dxf.close()
