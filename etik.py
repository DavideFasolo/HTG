import math
def dis_etichetta(cx,cy,cz,raggioforo,htesto,angolo,livello,nume,colore='0',dmodA=1.9,dmodB=1.2,spessore=0,appros=4):
        htesto=float(htesto)
        if float(nume)>9:
                dtesto=htesto*dmodA
        else:
                dtesto=htesto*dmodB
        #print(nume)
        etl=round(dtesto*math.tan(math.pi/8),4)
        polyetl=list()
        lato=list()
        #p0
        lato.append(round(cx+raggioforo*math.cos(angolo*math.pi/180),appros))
        lato.append(round(cy+raggioforo*math.sin(angolo*math.pi/180),appros))
        lato.append(round(cz,appros))
        polyetl.append(lato)
        lato=list()
        #p1
        lato.append(round(cx+(raggioforo+etl)*math.cos(angolo*math.pi/180)-etl/2,appros))
        lato.append(round(cy+(raggioforo+etl)*math.sin(angolo*math.pi/180),appros))
        lato.append(round(cz,appros))
        polyetl.append(lato)
        lato=list()
        #p2
        lato.append(round(polyetl[1][0]-etl*math.sin(math.pi/4),appros))
        lato.append(round(polyetl[1][1]+etl*math.sin(math.pi/4),appros))
        lato.append(round(cz,appros))
        polyetl.append(lato)
        lato=list()
        #p3
        lato.append(round(polyetl[2][0],appros))
        lato.append(round(polyetl[2][1]+etl,appros))
        lato.append(round(cz,appros))
        polyetl.append(lato)
        lato=list()
        #p4
        lato.append(round(polyetl[3][0]+etl*math.sin(math.pi/4),appros))
        lato.append(round(polyetl[3][1]+etl*math.sin(math.pi/4),appros))
        lato.append(round(cz,appros))
        polyetl.append(lato)
        lato=list()
        #p5
        lato.append(round(polyetl[4][0]+etl,appros))
        lato.append(round(polyetl[4][1],appros))
        lato.append(round(cz,appros))
        polyetl.append(lato)
        lato=list()
        #p6
        lato.append(round(polyetl[5][0]+etl*math.sin(math.pi/4),appros))
        lato.append(round(polyetl[5][1]-etl*math.sin(math.pi/4),appros))
        lato.append(round(cz,appros))
        polyetl.append(lato)
        lato=list()
        #p7
        lato.append(round(polyetl[6][0],appros))
        lato.append(round(polyetl[6][1]-etl,appros))
        lato.append(round(cz,appros))
        polyetl.append(lato)
        lato=list()
        #p8
        lato.append(round(polyetl[7][0]-etl*math.sin(math.pi/4),appros))
        lato.append(round(polyetl[7][1]-etl*math.sin(math.pi/4),appros))
        lato.append(round(cz,appros))
        polyetl.append(lato)
        lato=list()
        #p9(==p0)
        lato.append(round(polyetl[0][0],appros))
        lato.append(round(polyetl[0][1],appros))
        lato.append(round(cz,appros))
        polyetl.append(lato)
        lato=list()
        ii=0
        linea=str()
        etiket=str()
        while ii<(len(polyetl)-1):
                linea=('0\nLINE\n8\n'
                       +livello
                       +'\n10\n'
                       +str(polyetl[ii][0])
                       +'\n20\n'
                       +str(polyetl[ii][1])
                       +'\n30\n'
                       +str(polyetl[ii][2])
                       +'\n11\n'
                       +str(polyetl[ii+1][0])
                       +'\n21\n'
                       +str(polyetl[ii+1][1])
                       +'\n31\n'
                       +str(polyetl[ii+1][2])
                       +'\n62\n'
                       +colore
                       +'\n')
                etiket+=linea
                ii+=1
        return etiket;
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
