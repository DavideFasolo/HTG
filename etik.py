import math
def coord_testo_etichetta(cx,cy,cz,raggioforo,htesto,angolo,coordinata,nume,dmodA=1.9,dmodB=1.2,etk_dmodAc=1.6,etk_dmodBc=2):
        htesto=float(htesto)
        if float(nume)>9:
                dtesto=htesto*dmodA
        else:
                dtesto=htesto*dmodB
        etl=round(dtesto*math.tan(math.pi/8),4)
        polyetl=list()
        lato=list()
        #p0(p1)
        lato.append(round(cx+(raggioforo+etl)*math.cos(angolo*math.pi/180)-etl/2,4))
        lato.append(round(cy+(raggioforo+etl)*math.sin(angolo*math.pi/180),4))
        lato.append(round(cz,4))
        polyetl.append(lato)
        lato=list()
        #p1(p2)
        lato.append(round(polyetl[0][0]-etl*math.sin(math.pi/4),4))
        lato.append(round(polyetl[0][1]+etl*math.sin(math.pi/4),4))
        lato.append(round(cz,4))
        polyetl.append(lato)
        lato=list()
        if coordinata=='x':
                if nume>9:
                        etikoord=polyetl[0][0]-(polyetl[0][0]-polyetl[1][0])/etk_dmodAc
                else:
                        etikoord=polyetl[0][0]-(polyetl[0][0]-polyetl[1][0])/etk_dmodBc
        if coordinata=='y':
                if nume>9:
                        etikoord=polyetl[0][1]-(polyetl[0][1]-polyetl[1][1])/etk_dmodAc
                else:
                        etikoord=polyetl[0][1]-(polyetl[0][1]-polyetl[1][1])/etk_dmodBc
        return etikoord;
