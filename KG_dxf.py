import math


class DxfFormat:
    def __init__(self, f: str):
        self.dxf_start = '999\nFile "' + str(f) + '" esportato tramite "Hole Table Generator" by "Kill Goliath"\n'
        self.dxf_start += '999\nPowered by Davide Fasolo 2018\n'
        self.dxf_start += '0\nSECTION\n'
        self.dxf_start += '2\nENTITIES\n'
        ##############
        self.dxf_end = '0\nENDSEC\n0\nEOF'


class Punto:
    def __init__(self, c_x: float = 0, c_y: float = 0, c_z: float = 0):
        self.x = c_x
        self.y = c_y
        self.z = c_z


class Linea:
    def __init__(self, x1: float = 0, y1: float = 0, x2: float = 0, y2: float = 0, livello: str = 'assi', colore: int = 0):
        self.P1 = Punto(float(x1), float(y1))
        self.P2 = Punto(float(x2), float(y2))
        self.dxfcode = '0\nLINE\n8\n'
        self.dxfcode += str(livello)
        self.dxfcode += '\n10\n'
        self.dxfcode += str(x1)
        self.dxfcode += '\n20\n'
        self.dxfcode += str(y1)
        self.dxfcode += '\n11\n'
        self.dxfcode += str(x2)
        self.dxfcode += '\n21\n'
        self.dxfcode += str(y2)
        if colore:
            self.dxfcode += '\n62\n'
            self.dxfcode += str(colore)
        self.dxfcode += '\n'


class Cerchio:
    def __init__(self, point: Punto, cr: float = 0, livello: str = 'Fori', colore: int = 0):
        self.centro = point
        self.raggio = cr
        self.diametro = cr * 2
        self.dxfcode = '0\nCIRCLE\n8\n{0}\n10\n{1}\n20\n{2}\n30\n{3}\n40\n{4}\n62\n{5}\n'\
            .format(livello, self.centro.x, self.centro.y, self.centro.z, cr, colore)

    def min_x(self):
        return self.centro.x - self.raggio

    def min_y(self):
        return self.centro.y - self.raggio

    def max_x(self):
        return self.centro.x + self.raggio

    def max_y(self):
        return self.centro.y + self.raggio


class Testo:
    def __init__(self, cx: float = 0, cy: float = 0, cz: float = 0, ofx: float = 0, ofy: float = 0, stringa: int = 100, h: float = 3.5,
                 livello: str = 'numeri', colore: int = 0):
        self.padx = float(ofx)
        self.pady = float(ofy)
        self.valore = str(stringa)
        self.caratteri = len(str(stringa))
        self.dimensione = float(h)
        self.origine = Punto(float(cx) + self.padx, float(cy) + self.pady, float(cz))
        self.dxfcode = '0\nTEXT\n8\n'
        self.dxfcode += str(livello)
        self.dxfcode += '\n10\n'
        self.dxfcode += str(self.origine.x)
        self.dxfcode += '\n20\n'
        self.dxfcode += str(self.origine.y)
        self.dxfcode += '\n30\n'
        self.dxfcode += str(self.origine.z)
        self.dxfcode += '\n40\n'
        self.dxfcode += str(self.dimensione)
        self.dxfcode += '\n1\n'
        self.dxfcode += str(self.valore)
        if colore:
            self.dxfcode += '\n62\n'
            self.dxfcode += str(colore)
        self.dxfcode += '\n'


class Etichetta:
    def __init__(self, nume: int = 100, htesto: float = 3.5, px: float = 0, py: float = 0, pz: float = 0,
                 angolo: float = 20, coloretik: int = 0, livelloetik: str = 'etichette', appros: int = 4):
        dmd_a = 2.6
        dmd_b = 2.1
        dmd_c = 1.6
        htesto = float(htesto)
        if float(nume) > 99:
            dtesto = htesto * dmd_a
        else:
            if float(nume) > 9:
                dtesto = htesto * dmd_b
            else:
                dtesto = htesto * dmd_c
        self.lato = round(dtesto * math.tan(math.pi / 8), 4)
        self.P0 = Punto(round(px, appros),
                        round(py, appros),
                        round(pz, appros))
        self.P1 = Punto(round(px + self.lato * math.cos(angolo * math.pi / 180) - self.lato / 2, appros),
                        round(py + self.lato * math.sin(angolo * math.pi / 180), appros),
                        self.P0.z)
        self.P2 = Punto(round(self.P1.x - self.lato * math.sin(math.pi / 4), appros),
                        round(self.P1.y + self.lato * math.sin(math.pi / 4), appros),
                        self.P0.z)
        self.P3 = Punto(round(self.P2.x, appros),
                        round(self.P2.y + self.lato, appros),
                        self.P0.z)
        self.P4 = Punto(round(self.P3.x + self.lato * math.sin(math.pi / 4), appros),
                        round(self.P3.y + self.lato * math.sin(math.pi / 4), appros),
                        self.P0.z)
        self.P5 = Punto(round(self.P4.x + self.lato, appros),
                        round(self.P4.y, appros),
                        self.P0.z)
        self.P6 = Punto(round(self.P5.x + self.lato * math.sin(math.pi / 4), appros),
                        round(self.P5.y - self.lato * math.sin(math.pi / 4), appros),
                        self.P0.z)
        self.P7 = Punto(round(self.P6.x, appros),
                        round(self.P6.y - self.lato, appros),
                        self.P0.z)
        self.P8 = Punto(round(self.P7.x - self.lato * math.sin(math.pi / 4), appros),
                        round(self.P7.y - self.lato * math.sin(math.pi / 4), appros),
                        self.P0.z)
        self.P9 = Punto(self.P0.x, self.P0.y, self.P0.z)

        if int(nume) > 9:
            self.padx = self.lato / math.sqrt(2) / 2.8
        else:
            self.padx = self.lato / math.sqrt(2) / 2.3
        self.pady = 0 - (float(htesto) - self.lato) / 2
        i = 0
        self.dxfcode = str()
        while i < 9:
            self.dxfcode += '0\nLINE\n8\n'
            self.dxfcode += str(livelloetik)
            self.dxfcode += '\n10\n'
            self.dxfcode += str(eval('self.P%d.x' % i))
            self.dxfcode += '\n20\n'
            self.dxfcode += str(eval('self.P%d.y' % i))
            self.dxfcode += '\n30\n'
            self.dxfcode += str(eval('self.P%d.z' % i))
            self.dxfcode += '\n11\n'
            self.dxfcode += str(eval('self.P%d.x' % (i + 1)))
            self.dxfcode += '\n21\n'
            self.dxfcode += str(eval('self.P%d.y' % (i + 1)))
            self.dxfcode += '\n31\n'
            self.dxfcode += str(eval('self.P%d.z' % (i + 1)))
            self.dxfcode += '\n62\n'
            self.dxfcode += str(coloretik)
            self.dxfcode += '\n'
            i += 1


class Forotag:
    def __init__(self, circle: Cerchio, htesto: float = 3.5,
                 angolo: float = 20, nume: int = 2, appros: int = 4, colorecer: int = 0, livellocer: str = 'cerchi',
                 coloretik: int = 0, livelloetik: str = 'etichette', livellotes: str = 'testo', coloretes: int = 0):
        self.centro = circle.centro
        self.cerchio = Cerchio(self.centro, circle.raggio, livellocer, colorecer)
        self.etichetta = Etichetta(nume, htesto,
                                   round(self.centro.x + self.cerchio.raggio * math.cos(angolo * math.pi / 180),
                                         appros),
                                   round(self.centro.y + self.cerchio.raggio * math.sin(angolo * math.pi / 180),
                                         appros),
                                   self.centro.z, angolo, coloretik, livelloetik, appros)
        self.testo = Testo(self.etichetta.P2.x, self.etichetta.P2.y, self.etichetta.P2.z,
                           self.etichetta.padx, self.etichetta.pady, nume, htesto, livellotes, coloretes)

        self.dxfcode = self.cerchio.dxfcode + self.etichetta.dxfcode + self.testo.dxfcode
