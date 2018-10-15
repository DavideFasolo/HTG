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
        proprio.dxfcode += '0\nLINE\n8\n'
        proprio.dxfcode += str(y1)
        proprio.dxfcode += '\n11\n'
        proprio.dxfcode += str(x2)
        proprio.dxfcode += '\n21\n'
        proprio.dxfcode += str(y2)
        if colore:
            proprio.dxfcode += '\n62\n'
            proprio.dxfcode += colore
        proprio.dxfcode += '\n'


class cerchio:
    def __init__(proprio,cx, cy, cz, cr, livello, colore=0):
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

def dxf_testo(cx, cy, cz, ofx, ofy, caratteri, h, livello, colore=0, spessore=0):
    testo = '0\nTEXT\n8\n'
    testo += livello
    testo += '\n10\n'
    testo += str(cx + ofx)
    testo += '\n20\n'
    testo += str(cy + ofy)
    testo += '\n30\n'
    testo += str(cz)
    testo += '\n40\n'
    testo += h
    testo += '\n1\n'
    testo += caratteri
    if colore:
        testo += '\n62\n'
        testo += colore
    testo += '\n8\n'
    testo += livello
    if spessore:
        testo += '\n39\n'
        testo += spessore
    testo += '\n'
    return testo;
