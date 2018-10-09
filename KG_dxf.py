def dxf_linea(x1,y1,z1,x2,y2,z2,livello,colore=0,spessore=0):
    linea='0\nLINE\n8\n'
    linea+=livello
    linea+='\n10\n'
    linea+=str(x1)
    linea+='\n20\n'
    linea+=str(y1)
    linea+='\n11\n'
    linea+=str(x2)
    linea+='\n21\n'
    linea+=str(y2)
    if colore:
        linea+='\n62\n'
        linea+=colore
    if spessore:
        linea+='\n39\n'
        linea+=spessore
    linea+='\n'
    return linea;

def dxf_cerchio(cx,cy,cz,cr,livello,colore=0,spessore=0):
    cerchio='0\nCIRCLE\n8\n'
    cerchio+=livello
    cerchio+='\n10\n'
    cerchio+=str(cx)
    cerchio+='\n20\n'
    cerchio+=str(cy)
    cerchio+='\n30\n'
    cerchio+=str(cz)
    cerchio+='\n40\n'
    cerchio+=str(cr)
    if colore:
        cerchio+='\n62\n'
        cerchio+=colore
    if spessore:
        cerchio+='\n39\n'
        cerchio+=spessore
    cerchio+='\n'
    return cerchio;

def dxf_testo(cx,cy,cz,ofx,ofy,caratteri,h,livello,colore=0,spessore=0):
    testo='0\nTEXT\n8\n'
    testo+=livello
    testo+='\n10\n'
    testo+=str(cx+ofx)
    testo+='\n20\n'
    testo+=str(cy+ofy)
    testo+='\n30\n'
    testo+=str(cz)
    testo+='\n40\n'
    testo+=h
    testo+='\n1\n'
    testo+=caratteri
    if colore:
        testo+='\n62\n'
        testo+=colore
    testo+='\n8\n'
    testo+=livello
    if spessore:
        testo+='\n39\n'
        testo+=spessore
    testo+='\n'
    return testo;
