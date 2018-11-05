import configparser

CONFIGURATION_FILENAME = "config.kg"
POST_FILENAME = "ppc.kg"


class HtgConfiguration:
    def __init__(self, path):
        self.path = path + CONFIGURATION_FILENAME
        self.Config = configparser.ConfigParser()
        self.Config.read(self.path)

    def reload(self):
        self.Config.read(self.path)

    def save(self):
        with open(self.path, 'w') as configfile:
            self.Config.write(configfile)


class StructConfig:
    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path + CONFIGURATION_FILENAME)
        self.round_val = config.getint('struct', 'floating point')


class DrawConfig:
    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path + CONFIGURATION_FILENAME)
        self.tag_angle = config.getfloat('draw', 'tag angle')
        self.text_height = config.getfloat('draw', 'tag text height')
        self.font_ratio = config.getfloat('draw', 'tag font ratio')


class DxfConfig:
    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path + CONFIGURATION_FILENAME)
        self.axis_name = config.get('dxf advanced parameters', 'axis style name')
        self.axis_description = config.get('dxf advanced parameters', 'axis style description')
        self.axis_pattern = list(map(float, config.get('dxf advanced parameters', 'axis dash pattern').split(' ')))
        self.tag_text_format = [
            config.getint('dxf advanced parameters', 'tag text align x'),
            config.getint('dxf advanced parameters', 'tag text align y'),
            config.getfloat('draw', 'tag text height'),
            config.getfloat('draw', 'tag font ratio')
        ]
        self.circle_level = config.get('levels', 'circle')
        self.axis_level = config.get('levels', 'axis')
        self.tag_level = config.get('levels', 'tag')
        self.text_level = config.get('levels', 'text')
        self.circle_color = config.getint('colors', 'circle')
        self.axis_color = config.getint('colors', 'axis')
        self.tag_color = config.getint('colors', 'tag')
        self.text_color = config.getint('colors', 'text')
        self.tag_angle = config.getfloat('draw', 'tag angle')


class ColorConfig:
    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path + CONFIGURATION_FILENAME)
        self.circle_color = config.getint('colors', 'circle')
        self.axis_color = config.getint('colors', 'axis')
        self.tag_color = config.getint('colors', 'tag')
        self.text_color = config.getint('colors', 'text')
        
        
class LevelAndColorConfig:
    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path + CONFIGURATION_FILENAME)
        self.circle_level = config.get('levels', 'circle')
        self.axis_level = config.get('levels', 'axis')
        self.tag_level = config.get('levels', 'tag')
        self.text_level = config.get('levels', 'text')
        self.circle_color = config.getint('colors', 'circle')
        self.axis_color = config.getint('colors', 'axis')
        self.tag_color = config.getint('colors', 'tag')
        self.text_color = config.getint('colors', 'text')


class CsvConfig:
    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path + CONFIGURATION_FILENAME)
        self.separator = config.get('csv export', 'separator')
        self.d_mark = config.get('csv export', 'decimal mark')


class Ppcs:
    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path + POST_FILENAME)
        self.plist = config.get('avaiable ppcs', 'ppcs').split(',')


class PostProcessor:
    def __init__(self, path, ppc_name):
        config = configparser.ConfigParser()
        config.read(path + 'ppcs\\' + ppc_name)


######################################################################
class InterfaceConfiguration:
    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path + CONFIGURATION_FILENAME)

        self.arrot = config.getint('ambiente', 'cifre decimali delle coordinate')
        self.traduttore = config.get('postprocessore cnc', 'nome postprocessore')
        self.separ = config.get('formattazione csv', 'separatore colonne')
        self.virgo = config.get('formattazione csv', 'virgola')


class DrawingExchangeFormatConfigurations:
    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path + CONFIGURATION_FILENAME)

        self.coord_z = config.get('ambiente', 'esporta coordinate Z dei cerchi')
        self.cer_livello = config.get('stile cerchi', 'livello')
        self.cer_colore = config.get('stile cerchi', 'colore del tratto')
        self.ass_colore = config.get('stile assi', 'colore tratto')
        self.htesto = config.get('stile etichette', 'altezza caratteri')
        self.tes_livello = config.get('stile etichette', 'livello testo')
        self.tes_colore = config.get('stile etichette', 'colore testo')
        self.angolo = config.getfloat('stile etichette', 'angolazione')
        self.etk_livello = config.get('stile etichette', 'livello')
        self.etk_colore = config.get('stile etichette', 'colore tratto')
        self.etk_dmodA = config.getfloat('avanzate', 'scala dimensioni testo due cifre')
        self.etk_dmodB = config.getfloat('avanzate', 'scala dimensioni testo una cifra')
        self.etk_dmodAx = config.getfloat('avanzate', 'fattore offset tag due cifre x')
        self.etk_dmodAy = config.getfloat('avanzate', 'fattore offset tag due cifre y')
        self.etk_dmodBx = config.getfloat('avanzate', 'fattore offset tag una cifra x')
        self.etk_dmodBy = config.getfloat('avanzate', 'fattore offset tag una cifra y')


class PostProcessorConfiguration:
    def __init__(self, path, translator):
        config = configparser.ConfigParser()
        config.read(path + translator + "\\" + translator + ".pp")
        print(path + translator + "\\" + translator + ".pp")

        self.enne = config.get('generale', 'identificatore riga')
        self.incremento_N = config.getint('generale', 'incremento riga')
        self.zzz = config.get('generale', 'Z di arrivo comune')
        self.rigaforo = config.get('generale', 'riga di foratura')
        self.vt = config.getfloat('generale', 'velocita di taglio')
        self.giriminuto = config.get('generale', 'giri al minuto')


class TextConfiguration:
    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path + CONFIGURATION_FILENAME)

        self.etcoord = config.get('formattazione txt', 'etichette coordinate')
        self.z_coord = config.get('formattazione txt', 'coordinate z')
        self.intestaz = config.get('formattazione txt', 'intestazione')
