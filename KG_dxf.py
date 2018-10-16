import math
class punto:
    def __init__(proprio,cX,cY,cZ=0):
        proprio.x=cX
        proprio.y=cY
        proprio.z=cZ

class linea:
    def __init__(proprio, x1, y1, x2, y2, livello=0, colore=0):
        proprio.P1=punto(float(x1),float(y1))
        proprio.P2=punto(float(x2),float(y2))
        proprio.dxfcode = '0\nLINE\n8\n'
        proprio.dxfcode += livello
        proprio.dxfcode += '\n10\n'
        proprio.dxfcode += str(x1)
        proprio.dxfcode += '\n20\n'
        proprio.dxfcode += str(y1)
        proprio.dxfcode += '\n11\n'
        proprio.dxfcode += str(x2)
        proprio.dxfcode += '\n21\n'
        proprio.dxfcode += str(y2)
        if colore:
            proprio.dxfcode += '\n62\n'
            proprio.dxfcode += colore
        proprio.dxfcode += '\n'


class Cerchio:
    def __init__(proprio,cx, cy, cz, cr, livello, colore='0'):
        proprio.centro=punto(float(cx),float(cy),float(cz))
        proprio.raggio=float(cr)
        proprio.diametro=cr*2
        proprio.dxfcode = '0\nCIRCLE\n8\n'
        proprio.dxfcode += livello
        proprio.dxfcode += '\n10\n'
        proprio.dxfcode += str(cx)
        proprio.dxfcode += '\n20\n'
        proprio.dxfcode += str(cy)
        proprio.dxfcode += '\n30\n'
        proprio.dxfcode += str(cz)
        proprio.dxfcode += '\n40\n'
        proprio.dxfcode += str(cr)
        if colore:
            proprio.dxfcode += '\n62\n'
            proprio.dxfcode += colore
        proprio.dxfcode += '\n'

class Testo:
    def __init__(proprio,cx, cy, ofx, ofy, stringa, h, livello, colore='0'):
        proprio.padx=float(ofx)
        proprio.pady=float(ofy)
        proprio.valore=str(stringa)
        proprio.caratteri=len(str(stringa))
        proprio.dimensione=float(h)
        proprio.origine=punto(float(cx+proprio.padx),float(cy+proprio.pady))
        proprio.dxfcode = '0\nTEXT\n8\n'
        proprio.dxfcode += livello
        proprio.dxfcode += '\n10\n'
        proprio.dxfcode += str(proprio.origine.x)
        proprio.dxfcode += '\n20\n'
        proprio.dxfcode += str(proprio.origine.y)
        proprio.dxfcode += '\n40\n'
        proprio.dxfcode += str(proprio.dimensione)
        proprio.dxfcode += '\n1\n'
        proprio.dxfcode += str(proprio.valore)
        if colore:
            proprio.dxfcode += '\n62\n'
            proprio.dxfcode += colore
        proprio.dxfcode += '\n'

class Etichetta:
    def __init__(proprio, nume=100, htesto=3.5, px=0, py=0, pz=0, angolo=20, coloretik='0', livelloetik='etichette', appros=4):
        dmodA=2.6
        dmodB=2.1
        dmodC=1.6
        htesto = float(htesto)
        if float(nume) > 99:
            dtesto = htesto * dmodA
        else:
            if float(nume) > 9:
                dtesto = htesto * dmodB
            else:
                dtesto = htesto * dmodC
        proprio.lato = round(dtesto * math.tan(math.pi / 8), 4)
        proprio.P0 = punto(round(px,appros),
                           round(py,appros),
                           round(pz,appros))
        proprio.P1 = punto(round(px + proprio.lato * math.cos(angolo * math.pi / 180) - proprio.lato / 2, appros),
                            round(py + proprio.lato * math.sin(angolo * math.pi / 180), appros),
                            proprio.P0.z)
        proprio.P2 = punto(round(proprio.P1.x - proprio.lato * math.sin(math.pi / 4), appros),
                           round(proprio.P1.y + proprio.lato * math.sin(math.pi / 4), appros),
                           proprio.P0.z)
        proprio.P3 = punto(round(proprio.P2.x, appros),
                           round(proprio.P2.y + proprio.lato, appros),
                           proprio.P0.z)
        proprio.P4 = punto(round(proprio.P3.x + proprio.lato * math.sin(math.pi / 4), appros),
                           round(proprio.P3.y + proprio.lato * math.sin(math.pi / 4), appros),
                           proprio.P0.z)
        proprio.P5 = punto(round(proprio.P4.x + proprio.lato, appros),
                           round(proprio.P4.y, appros),
                           proprio.P0.z)
        proprio.P6 = punto(round(proprio.P5.x + proprio.lato * math.sin(math.pi / 4), appros),
                           round(proprio.P5.y - proprio.lato * math.sin(math.pi / 4), appros),
                           proprio.P0.z)
        proprio.P7 = punto(round(proprio.P6.x, appros),
                           round(proprio.P6.y - proprio.lato, appros),
                           proprio.P0.z)
        proprio.P8 = punto(round(proprio.P7.x - proprio.lato * math.sin(math.pi / 4), appros),
                           round(proprio.P7.y - proprio.lato * math.sin(math.pi / 4), appros),
                           proprio.P0.z)
        proprio.P9 = punto(proprio.P0.x, proprio.P0.y, proprio.P0.z)

        if nume>9:
            proprio.padx=proprio.lato / math.sqrt(2) /2.8
        else:
            proprio.padx = proprio.lato / math.sqrt(2) / 2.3
        proprio.pady=0-(htesto-proprio.lato)/2
        i = 0
        proprio.dxfcode = str()
        while i < 9:
            proprio.dxfcode += '0\nLINE\n8\n'
            proprio.dxfcode += livelloetik
            proprio.dxfcode += '\n10\n'
            proprio.dxfcode += str(eval('proprio.P%d.x' % i))
            proprio.dxfcode += '\n20\n'
            proprio.dxfcode += str(eval('proprio.P%d.y' % i))
            proprio.dxfcode += '\n11\n'
            proprio.dxfcode += str(eval('proprio.P%d.x' % (i + 1)))
            proprio.dxfcode += '\n21\n'
            proprio.dxfcode += str(eval('proprio.P%d.y' % (i + 1)))
            proprio.dxfcode += '\n62\n'
            proprio.dxfcode += coloretik
            proprio.dxfcode += '\n'
            i += 1

class Forotag:
    def __init__(proprio,cx=0, cy=0, cz=0, raggioforo=2, htesto=3.5, angolo=20, nume=2,appros=4, colorecer='0',
                 livellocer='cerchi',coloretik='0',livelloetik='etichette',livellotes='testo',coloretes='0'):
        proprio.centro=punto(round(cx,appros),round(cy,appros),round(cz,appros))
        proprio.cerchio=Cerchio(proprio.centro.x,proprio.centro.y,proprio.centro.z,raggioforo,livellocer,colorecer)
        proprio.etichetta=Etichetta(nume,htesto,
                                    round(proprio.centro.x + proprio.cerchio.raggio * math.cos(angolo * math.pi / 180), appros),
                                    round(proprio.centro.y + proprio.cerchio.raggio * math.sin(angolo * math.pi / 180), appros),
                                    proprio.centro.z,angolo,coloretik,livelloetik,appros)
        proprio.testo=Testo(proprio.etichetta.P2.x,proprio.etichetta.P2.y,
                            proprio.etichetta.padx,proprio.etichetta.pady,nume,htesto,livellotes,coloretes)

        proprio.dxfcode=proprio.cerchio.dxfcode+proprio.etichetta.dxfcode+proprio.testo.dxfcode

foroforo=Forotag()
print(foroforo.dxfcode)