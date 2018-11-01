from KG_dxf_lib import *
from minmax import *
from infrastructure import *


#                                                                                                                      _
#                                                       FILE                                                           _
#                                                                                                                      _


def file_get_full_name(p):
    return p.split('/').pop()


def file_get_name(f):
    return file_get_full_name(f).split('.')[0]


def file_get_ext(f):
    return '.' + file_get_full_name(f).split('.')[1]


def path_map(p):
    return map(lambda s: '{0}/'.format(s), p.split('/')[0:-1])


def path_get(p):
    return ''.join(path_map(p)).rstrip('/')


def file_read(file):
    return open(file, "r").readlines()


#                                                                                                                      _
#                                                  PARSER VDA                                                          _
#                                                                                                                      _


def round_value():
    try:
        int(struct_conf.round_val)
    except NameError:
        print('Valore di approssimazione non trovato')
        print('verrà usato un default di 3 cifre decimali')
        return 3
    else:
        return int(struct_conf.round_val)


def round_var(v): return round(float(v), round_value())


def circle_check(s):
    return s.count("CIRCLE /" or
                   "CIRCLE/")


def circle_line_check(s):
    return s.count(",") <= 11 and s[-1] == ","


def arrange_hole(s):
    return [round_var(s.split(',')[3]) * 2, list(map(round_var, s.split(',')))[0:-9]]


def strip_first(s):
    return s[s.find("/") + 1:72].strip()


def strip_next(s):
    return s[0:72].strip()


def parse_vda(vda_read):
    vda_read = vda_read[21:-1]
    parsed = list()
    i = 0
    while i < len(vda_read):
        if circle_check(vda_read[i]):
            hole = strip_first(vda_read[i])
            g = 1
            while circle_line_check(hole):
                hole += strip_next(vda_read[i + g])
                g += 1
            parsed.append(arrange_hole(hole))
        i += 1
    return parsed


def clean_and_sort(parsed):
    clean = [x for n, x in enumerate(parsed) if x not in parsed[:n]]
    clean.sort()
    return clean


def hole_matrix(li):
    fori_group = list()
    num_hole = 0
    act_diam = 0
    diam_count = 0
    for something in li:
        if num_hole == 0:
            act_diam = something[0]
            num_hole += 1
            fori_group.append([act_diam, [[num_hole, something[1]]]])
        else:
            if act_diam == something[0]:
                num_hole += 1
                fori_group[diam_count][1].append([num_hole, something[1]])
            else:
                act_diam = something[0]
                num_hole += 1
                fori_group.append([act_diam, [[num_hole, something[1]]]])
                diam_count += 1
    return fori_group


#                                                                                                                      _
#                                                   UTILITY                                                            _
#                                                                                                                      _


def len_matrix(matrix):
    numero_fori = int()
    for gruppo in matrix:
        numero_fori += len(gruppo[1])
    return numero_fori


def len_num(matrix, c):
    length_a = int()
    length_b = int()
    for tabella in matrix:
        for foro in tabella[1]:
            length_a = max(length_a, len(str(foro[1][c]).split('.')[0]))
            length_b = max(length_b, len(str(foro[1][c]).split('.')[1]))
    return length_a, length_b


def arrange_coord(value, digits):
    value = str(value).split('.')
    if digits[0] > len(value[0]):
        value[0] = ' ' * (digits[0] - len(value[0])) + value[0]
    if digits[1] > len(value[1]):
        value[1] = value[1] + ' ' * (digits[1] - len(value[1]))
    return '.'.join(value)


#                                                                                                                      _
#                                                CHECK OUTPUT                                                          _
#                                                                                                                      _


def report_table(matrix):
    report = 'Trovati i seguenti ' + str(len_matrix(matrix)) + ' fori:\n\n'
    len_x = len_num(matrix, 0)
    len_y = len_num(matrix, 1)
    len_z = len_num(matrix, 2)
    for hole_group in matrix:
        report += 'N. {0} fori di diametro {1} mm:\n'.format(str(len(hole_group[1])),
                                                             str(hole_group[0]))
        for hole in hole_group[1]:
            hole_x = arrange_coord(hole[1][0], len_x)
            hole_y = arrange_coord(hole[1][1], len_y)
            hole_z = arrange_coord(hole[1][2], len_z)
            report += '{0}:\tx {1}\t\ty {2}\t\tz {3}\n'.format(str(hole[0]),
                                                               hole_x,
                                                               hole_y,
                                                               hole_z)
        report += '\n'
    return report


#                                                                                                                      _
#                                                CSV OUTPUT SETUP                                                      _
#                                                                                                                      _


def csv_value(value, decimal_mark): return str(value).replace('.', decimal_mark)


def csv_table(matrix, csv_config_parser):
    csv_export = 'Pos' + csv_config_parser.separator +\
                 'Ø' + csv_config_parser.separator +\
                 'X' + csv_config_parser.separator +\
                 'Y' + csv_config_parser.separator +\
                 'Z' + '\n'
    for hole_group in matrix:
        for hole in hole_group[1]:
            csv_export += csv_value(hole[0], csv_config_parser.d_mark) + csv_config_parser.separator +\
                          csv_value(hole_group[0], csv_config_parser.d_mark) + csv_config_parser.separator +\
                          csv_value(hole[1][0], csv_config_parser.d_mark) + csv_config_parser.separator +\
                          csv_value(hole[1][1], csv_config_parser.d_mark) + csv_config_parser.separator +\
                          csv_value(hole[1][2], csv_config_parser.d_mark) + '\n'
    return csv_export


def color(aci): return aci, file_read(workpath + 'aci_colors.kg')[aci][:-1]


#                                                                                                                      _
#                                               DXF OUTPUT SETUP                                                       _
#                                                                                                                      _


workpath = os.getcwd() + '\\Configurazione\\'
filename = 'C:\\Users\\Amon\Documents\\coding\\HTG\\filetestarea\\test.vda'
color_conf = ColorConfig(workpath)
level_conf = LevelConfig(workpath)
draw_conf = DrawConfig(workpath)
dxf_conf = DxfConfig(workpath)


def dxf_out_header_comments(filename_comment):
    return "{0}{1}{2}".format(
        dxf_comment('Hole Table Generator by KG-Soft')[1:],
        dxf_comment('Davide Fasolo 2018'),
        dxf_comment('pianta fori da file "' + filename_comment + '"')
    )


def dxf_out_tables():
    return dxf_section(
        dxf_tables(
            dxf_table(
                dxf_ltype_table(
                    dxf_dash_style(dxf_conf.axis_name,
                                   dxf_conf.axis_description,
                                   dxf_conf.axis_pattern)
                )
            )
        )
    )


def dxf_draw_axes(point_matrix, axis_level, axis_color, axis_style):
    return '{0}{1}'.format(dxf_line([get_min_x(point_matrix), 0, 0],
                                    [get_max_x(point_matrix), 0, 0],
                                    axis_level,
                                    axis_color,
                                    axis_style),
                           dxf_line([0, get_min_y(point_matrix), 0],
                                    [0, get_max_y(point_matrix), 0],
                                    axis_level,
                                    axis_color,
                                    axis_style))


def dxf_draw_entities(hole_matrix_out):
    dxf_out = str()
    for tabella in hole_matrix_out:
        dxf_out += '{0}{1}'.format(dxf_comment('#'*80),
                                   dxf_comment('N°{0} fori di diametro {1}'.format(str(len(tabella[1])),
                                                                                   str(tabella[0]))))
        for foro in tabella[1]:
            tag_matrix = tag_point_matrix(foro[1], tabella[0], draw_conf.tag_angle, foro[0])
            dxf_out += dxf_comment('#' * 28)
            dxf_out += dxf_comment('foro N°{0} Ø{1}'.format(str(foro[0]),
                                                            str(tabella[0])))
            dxf_out += dxf_circle(tabella[0],
                                  foro[1],
                                  level_conf.circle_level,
                                  color_conf.circle_color)
            dxf_out += dxf_polyline(tag_matrix[0],
                                    level_conf.tag_level,
                                    color_conf.tag_color)
            dxf_out += dxf_text(foro[0], tag_matrix[1],
                                dxf_conf.tag_text_format,
                                level_conf.text_level,
                                color_conf.text_color)
    dxf_out += dxf_draw_axes(hole_matrix_out, level_conf.axis_level, color_conf.axis_color, dxf_conf.axis_name)
    return dxf_section(dxf_entities(dxf_out))


def dxf_structure(entities_matrix, heading_filename):
    return '{0}{1}{2}{3}'.format(dxf_out_header_comments(heading_filename),
                                 dxf_out_tables(),
                                 dxf_draw_entities(entities_matrix),
                                 dxf_footer())


###################################################################################################
struct_conf = StructConfig(workpath)
csv_conf = CsvConfig(workpath)

matrice = hole_matrix(clean_and_sort(parse_vda(file_read(filename))))


print(report_table(matrice))


out_csv = open('C:\\Users\\Amon\\Desktop\\asd.csv', 'w+')
out_csv.write(csv_table(matrice, csv_conf))
out_csv.close()
out_dxf = open('C:\\Users\\Amon\\Desktop\\asd.dxf', 'w+')
out_dxf.write(dxf_structure(matrice, filename))
out_dxf.close()

# http://paulbourke.net/dataformats/dxf/
