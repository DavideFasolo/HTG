from KG_dxf import Linea, Forotag, Punto, Cerchio
from infrastructure import DrawingExchangeFormatConfigurations


def crea_tab_fori(fori: list, config_dxf: DrawingExchangeFormatConfigurations):
    i = 0
    v = 0
    min_x = fori[i][1] - fori[i][0] / 2
    max_x = fori[i][1] + fori[i][0] / 2
    min_y = fori[i][2] - fori[i][0] / 2
    max_y = fori[i][2] + fori[i][0] / 2
    fori_obj = list()
    fori_stesso_diam = list()
    while i < len(fori):
        point = Punto(round(float(fori[i][1]), 4),
                      round(float(fori[i][2]), 4),
                      round(float(fori[i][3] if config_dxf.coord_z else 0), 4))
        circle = Cerchio(point, fori[i][0] / 2)

        min_x = min(circle.min_x(), min_x)
        min_y = min(circle.min_y(), min_y)
        max_x = max(circle.max_x(), max_x)
        max_y = max(circle.max_y(), max_y)

        foro000 = Forotag(circle, config_dxf.htesto, config_dxf.angolo, i + 1, 4, config_dxf.cer_colore,
                          config_dxf.cer_livello, config_dxf.etk_colore, config_dxf.etk_livello,
                          config_dxf.tes_livello, config_dxf.tes_colore)

        if i == 0:
            fori_stesso_diam.append(foro000)
            fori_obj.append([circle.diametro, fori_stesso_diam])
        else:
            if circle.diametro != fori_obj[v][0]:
                fori_stesso_diam = [foro000]
                fori_obj.append([circle.diametro, fori_stesso_diam])
                v += 1
            else:
                if circle.diametro == fori_obj[v][0]:
                    fori_obj[v][1].append(foro000)
        i += 1
    asse_x = Linea(min_x, 0, max_x, 0, config_dxf.cer_livello, config_dxf.ass_colore)
    asse_y = Linea(0, min_y, 0, max_y, config_dxf.cer_livello, config_dxf.ass_colore)
    return fori_obj, assi(asse_x, asse_y)



class assi:
    def __init__(self, asse_x: Linea, asse_y: Linea):
        self.x = asse_x
        self.y = asse_y

    def min_x(self):
        return self.x.P1.x

    def max_x(self):
        return self.x.P2.x

    def min_y(self):
        return self.y.P1.y

    def max_y(self):
        return self.y.P2.y
