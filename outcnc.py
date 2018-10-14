import os
import configparser


class PostProcessorConfiguration:
    def __init__(self, path, translator):
        config = configparser.ConfigParser()
        config.read(path+translator+"\\"+translator+".pp")
        print(path+translator+"\\"+translator+".pp")
        print(os.getcwd())
        self.enne=str(config.get('generale','identificatore riga'))
        self.incremento_N=str(config.get('generale','incremento riga'))
        self.zzz=str(config.get('generale','Z di arrivo comune'))
        self.rigaforo=str(config.get('generale','riga di foratura'))
        self.vt=float(config.get('generale','velocita di taglio'))
        self.giriminuto=str(config.get('generale','giri al minuto'))


def esporta_cnc(fori,p,f,workpath,traduttore):
    cf = PostProcessorConfiguration(workpath, traduttore)

    dircnc=p+"\\"+f.strip(".")+"_cnc-forature"
    if not(os.path.exists(dircnc)):
        os.mkdir(dircnc)

    i=1
    diamtemp=list()
    n_fori_diam=list()
    diamtemp.append(fori[0][0])
    while i<len(fori)-1:
        diamtemp.append(fori[i][0])
        if diamtemp[i]==diamtemp[i-1]:
            contatore=str(diamtemp).count(str(diamtemp[i]))
        else:
            n_fori_diam.append([diamtemp[i-1],contatore])
            contatore=1
        i+=1
    n_fori_diam.append([diamtemp[i-1],contatore+1])

    i=0
    foro_attuale=0
    while i<len(n_fori_diam):
        diametro_format=str(float(n_fori_diam[i][0]))
        if round(float(diametro_format),0)-float(diametro_format)==0:
            diametro_format=int(round(float(diametro_format),0))
        cnc=dircnc+"\\"+f.strip(".")+"_Diam-"+str(diametro_format).replace(".",",")+".cnc"
        out_cnc = open(cnc,"w+")
        foro_sub_diam=0
        incremento_int=int(cf.incremento_N)
        while foro_sub_diam<n_fori_diam[i][1]:
            x=str(fori[foro_attuale+foro_sub_diam][1]).strip("0")
            y=str(fori[foro_attuale+foro_sub_diam][2]).strip("0")
            z=str(fori[foro_attuale+foro_sub_diam][3]).strip("0")
            nuforo=str(foro_attuale+foro_sub_diam+1)
            deforo=str(float(fori[foro_attuale+foro_sub_diam][0]))
            if cf.vt!=0:
                giriminuto=str(int(cf.vt*1000/(math.pi*float(fori[foro_attuale+foro_sub_diam][0]))))
            else:
                giriminuto=cf.giriminuto
            if cf.zzz!="no":
                z=cf.zzz
            scrivi_riga=cf.rigaforo.replace("<x>",x).replace("<y>",y).replace("<z>",z).replace("<s>",giriminuto).replace("<n>",nuforo).replace("<d>",deforo).split("#")
            cont_riga=0
            while cont_riga<len(scrivi_riga):
                out_cnc.write(cf.enne+"\t"+str(incremento_int)+"\t"+str(scrivi_riga[cont_riga])+"\n")
                incremento_int+=int(cf.incremento_N)
                cont_riga+=1
            foro_sub_diam+=1
        foro_attuale+=foro_sub_diam
        out_cnc.close()
        print("Creato il file \n"+cnc+"\n"+"Nella cartella dove si trova il file vda selezionato")
        i+=1


def esporta_txt(fori,p,f,workpath):

    class TextConfiguration:
        def __init__(self, path):
            Config = configparser.ConfigParser()
            Config.read(path+"config.kg")

            self.etcoord=str(Config.get('formattazione txt','etichette coordinate'))
            self.z_coord=str(Config.get('formattazione txt','coordinate z'))
            self.intestaz=str(Config.get('formattazione txt','intestazione'))

    cf = TextConfiguration(workpath)

    dirtxt=p+"\\"+f.strip(".")+"_txt-forature"
    if not(os.path.exists(dirtxt)):
        os.mkdir(dirtxt)

    i=1
    diamtemp=list()
    n_fori_diam=list()
    diamtemp.append(fori[0][0])
    while i<len(fori)-1:
        diamtemp.append(fori[i][0])
        if diamtemp[i]==diamtemp[i-1]:
            contatore=str(diamtemp).count(str(diamtemp[i]))
        else:
            n_fori_diam.append([diamtemp[i-1],contatore])
            contatore=1
        i+=1
    n_fori_diam.append([diamtemp[i-1],contatore+1])

    i=0
    foro_attuale=0
    while i<len(n_fori_diam):
        diametro_format=str(float(n_fori_diam[i][0]))
        if round(float(diametro_format),0)-float(diametro_format)==0:
            diametro_format=int(round(float(diametro_format),0))
        txt=dirtxt+"\\"+f.strip(".")+"_Diam-"+str(diametro_format).replace(".",",")+".txt"
        out_txt = open(txt,"w+")
        foro_sub_diam=0
        if cf.intestaz=='si':
            out_txt.write('Coordinate dei fori diametro '+str(diametro_format)+'\n\n')
        numiniz=str(foro_attuale+1)
        while foro_sub_diam<n_fori_diam[i][1]:
            x=str(fori[foro_attuale+foro_sub_diam][1]).strip("0")
            y=str(fori[foro_attuale+foro_sub_diam][2]).strip("0")
            z=str(fori[foro_attuale+foro_sub_diam][3]).strip("0")
            if cf.etcoord=='si':
                scrivi_riga='X'+x+'\t\t\tY'+y
                if cf.z_coord=='si':
                    scrivi_riga+='\t\t\tZ'+z+'\n'
                else:
                    scrivi_riga+='\n'
            else:
                scrivi_riga=x+'\t\t\t'+y
                if cf.z_coord=='si':
                    scrivi_riga+='\t\t\t'+z+'\n'
                else:
                    scrivi_riga+='\n'
            out_txt.write(scrivi_riga)
            foro_sub_diam+=1
        foro_attuale+=foro_sub_diam
        numfina=str(foro_attuale)
        if cf.intestaz=='si':
            out_txt.write('\n\nFori dal '+numiniz+' al '+numfina+' della tabella fori')
        out_txt.close()
        print("Creato il file \n"+txt+"\n"+"Nella cartella dove si trova il file vda selezionato")
        i+=1
