import configparser
import os


class HtgConfiguration:
    def __init__(self, path):
        self.path = path
        self.Config = configparser.ConfigParser()
        self.Config.read(path + "config.kg")

    def reload(self):
        self.Config.read(self.path + "config.kg")

    def save(self):
        with open(self.path+"config.kg", 'w') as configfile:
            self.Config.write(configfile)


class InterfaceConfiguration:
    def __init__(self, path):
        Config = configparser.ConfigParser()
        Config.read(path+"config.kg")

        self.arrot=int(Config.get('ambiente','cifre decimali delle coordinate'))
        self.traduttore=str(Config.get('postprocessore cnc','nome postprocessore'))
        self.separ=Config.get('formattazione csv','separatore colonne')
        self.virgo=Config.get('formattazione csv','virgola')


class DrawingExchangeFormatConfigurations:
    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path + "config.kg")

        self.coord_z=config.get('ambiente','esporta coordinate Z dei cerchi')
        self.cer_livello=str(config.get('stile cerchi','livello'))
        self.cer_colore=str(config.get('stile cerchi','colore del tratto'))
        self.ass_colore=str(config.get('stile assi','colore tratto'))
        self.htesto=str(config.get('stile etichette','altezza caratteri'))
        self.tes_livello=str(config.get('stile etichette','livello testo'))
        self.tes_colore=str(config.get('stile etichette','colore testo'))
        self.angolo=float(config.get('stile etichette','angolazione'))
        self.etk_livello=config.get('stile etichette','livello')
        self.etk_colore=str(config.get('stile etichette','colore tratto'))
        self.etk_dmodA=float(config.get('avanzate','scala dimensioni testo due cifre'))
        self.etk_dmodB=float(config.get('avanzate','scala dimensioni testo una cifra'))
        self.etk_dmodAx=float(config.get('avanzate','fattore offset tag due cifre x'))
        self.etk_dmodAy=float(config.get('avanzate','fattore offset tag due cifre y'))
        self.etk_dmodBx=float(config.get('avanzate','fattore offset tag una cifra x'))
        self.etk_dmodBy=float(config.get('avanzate','fattore offset tag una cifra y'))


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


class TextConfiguration:
    def __init__(self, path):
        Config = configparser.ConfigParser()
        Config.read(path+"config.kg")

        self.etcoord=str(Config.get('formattazione txt','etichette coordinate'))
        self.z_coord=str(Config.get('formattazione txt','coordinate z'))
        self.intestaz=str(Config.get('formattazione txt','intestazione'))