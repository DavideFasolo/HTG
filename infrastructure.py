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
        self.tag_stylename = config.get('dxf advanced parameters', 'tag text stylename')
        self.tag_font = config.get('draw', 'tag font')


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
        config.read(path + 'ppc\\' + ppc_name + '.ppc')
        self.name = config.get('identity', 'name')
        self.header = config.get('cnc structure', 'header')
        self.hole_line = config.get('cnc structure', 'hole line')
        self.footer = config.get('cnc structure', 'footer')
        self.cnc_F = config.get('defaults', 'cnc_F')
        self.cnc_S = config.get('defaults', 'cnc_S')
        self.cnc_I = config.get('defaults', 'cnc_I')
        self.cnc_Z = config.get('defaults', 'cnc_Z')
        self.cnc_Q = config.get('defaults', 'cnc_Q')
        self.cnc_Zf = config.get('defaults', 'cnc_Zf')
        self.cnc_J = config.get('defaults', 'cnc_J')
        self.com_header = config.get('comments', 'header')
        self.com_hole = config.get('comments', 'hole line')
        self.com_footer = config.get('comments', 'footer')
        self.line_nums = config.get('line format', 'numbers')
        self.line_step = config.getint('line format', 'line step')
        self.line_id = config.get('line format', 'line id').replace('____', '\t')
        self.separator = (config.get('line format', 'post number') == 'space' and ' ') or (config.get('line format', 'post number') == 'tab' and '\t') or (config.get('line format', 'post number') == 'none' and '')
        self.line_start = config.getint('line format', 'line start number')
        self.endline = config.get('line format', 'end line')
        self.lastline = config.get('line format', 'last line')
        self.z_true = config.get('switches', 'z head')
