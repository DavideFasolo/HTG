import os
import configparser
def esporta_cnc(fori,p,f,workpath,traduttore):

    postppc = configparser.ConfigParser()
    postppc.read(workpath+traduttore+"\\"+traduttore+".pp")
    print(workpath+traduttore+"\\"+traduttore+".pp")

    enne=str(postppc.get('generale','identificatore riga'))
    incenne=str(postppc.get('generale','incremento riga'))
    zzz=str(postppc.get('generale','Z di arrivo comune'))
    rigaforo=str(postppc.get('generale','riga di foratura'))
    vt=float(postppc.get('generale','velocita di taglio'))
    giriminuto=str(postppc.get('generale','giri al minuto'))

    dircnc=p+"\\"+f.strip(".")+"_cnc-forature"
    if not(os.path.exists(dircnc)):
        os.mkdir(dircnc)

    i=1
    vainmona=list()
    vainfiga=list()
    vainmona.append(fori[0][0])
    while i<len(fori)-1:
        vainmona.append(fori[i][0])
        if vainmona[i]==vainmona[i-1]:
            contatore=str(vainmona).count(str(vainmona[i]))
        else:
            vainfiga.append([vainmona[i-1],contatore])
            contatore=1
        i+=1
    vainfiga.append([vainmona[i-1],contatore+1])

    i=0
    contafiga=0
    while i<len(vainfiga):
        nomdia=str(float(vainfiga[i][0]))
        if round(float(nomdia),0)-float(nomdia)==0:
            nomdia=int(round(float(nomdia),0))
        cnc=dircnc+"\\"+f.strip(".")+"_Diam-"+str(nomdia).replace(".",",")+".cnc"
        out_cnc = open(cnc,"w+")
        figaebamba=0
        lelo=int(incenne)
        while figaebamba<vainfiga[i][1]:
            x=str(fori[contafiga+figaebamba][1]).strip("0")
            y=str(fori[contafiga+figaebamba][2]).strip("0")
            z=str(fori[contafiga+figaebamba][3]).strip("0")
            nuforo=str(contafiga+figaebamba+1)
            deforo=str(float(fori[contafiga+figaebamba][0]))
            if vt!=0:
                giriminuto=str(int(vt*1000/(math.pi*float(fori[contafiga+figaebamba][0]))))
            if zzz!="no":
                z=zzz
            fikah=rigaforo.replace("<x>",x).replace("<y>",y).replace("<z>",z).replace("<s>",giriminuto).replace("<n>",nuforo).replace("<d>",deforo).split("#")
            lalah=0
            while lalah<len(fikah):
                out_cnc.write(enne+"\t"+str(lelo)+"\t"+str(fikah[lalah])+"\n")
                lelo+=int(incenne)
                lalah+=1
            figaebamba+=1
        contafiga+=figaebamba
        out_cnc.close()
        print("Creato il file \n"+cnc+"\n"+"Nella cartella dove si trova il file vda selezionato")
        i+=1
def esporta_txt(fori,p,f,workpath):

    Config = configparser.ConfigParser()
    Config.read(workpath+"config.kg")

    etcoord=str(Config.get('formattazione txt','etichette coordinate'))
    z_coord=str(Config.get('formattazione txt','coordinate z'))
    intestaz=str(Config.get('formattazione txt','intestazione'))

    dirtxt=p+"\\"+f.strip(".")+"_txt-forature"
    if not(os.path.exists(dirtxt)):
        os.mkdir(dirtxt)

    i=1
    vainmona=list()
    vainfiga=list()
    vainmona.append(fori[0][0])
    while i<len(fori)-1:
        vainmona.append(fori[i][0])
        if vainmona[i]==vainmona[i-1]:
            contatore=str(vainmona).count(str(vainmona[i]))
        else:
            vainfiga.append([vainmona[i-1],contatore])
            contatore=1
        i+=1
    vainfiga.append([vainmona[i-1],contatore+1])

    i=0
    contafiga=0
    while i<len(vainfiga):
        nomdia=str(float(vainfiga[i][0]))
        if round(float(nomdia),0)-float(nomdia)==0:
            nomdia=int(round(float(nomdia),0))
        txt=dirtxt+"\\"+f.strip(".")+"_Diam-"+str(nomdia).replace(".",",")+".txt"
        out_txt = open(txt,"w+")
        figaebamba=0
        if intestaz=='si':
            out_txt.write('Coordinate dei fori diametro '+str(nomdia)+'\n\n')
        numiniz=str(contafiga+1)
        while figaebamba<vainfiga[i][1]:
            x=str(fori[contafiga+figaebamba][1]).strip("0")
            y=str(fori[contafiga+figaebamba][2]).strip("0")
            z=str(fori[contafiga+figaebamba][3]).strip("0")
            if etcoord=='si':
                fikah='X'+x+'\t\t\tY'+y
                if z_coord=='si':
                    fikah+='\t\t\tZ'+z+'\n'
                else:
                    fikah+='\n'
            else:
                fikah=x+'\t\t\t'+y
                if z_coord=='si':
                    fikah+='\t\t\t'+z+'\n'
                else:
                    fikah+='\n'
            out_txt.write(fikah)
            figaebamba+=1
        contafiga+=figaebamba
        numfina=str(contafiga)
        if intestaz=='si':
            out_txt.write('\n\nFori dal '+numiniz+' al '+numfina+' della tabella fori')
        out_txt.close()
        print("Creato il file \n"+txt+"\n"+"Nella cartella dove si trova il file vda selezionato")
        i+=1
