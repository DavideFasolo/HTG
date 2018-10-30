from infrastructure import *
import math


def file_get_full_name(p): return p.split('/').pop()


def file_get_name(f): return file_get_full_name(f).split('.')[0]


def file_get_ext(f): return '.' + file_get_full_name(f).split('.')[1]


def path_add_slash(s): return s + '/'


def path_get_list(p): return p.split('/')[0:-1]


def path_map(p): return map(path_add_slash, path_get_list(p))


def path_get(p): return ''.join(path_map(p)).rstrip('/')


def file_read(file): return open(file, "r").readlines()


def round_value(): return int(struct_conf.round_val)


def round_var(v): return round(float(v), round_value())


def circle_check(s):
    return s.count("CIRCLE /" or
                   "CIRCLE/")


def circle_line_check(s):
    return s.count(",") <= 11 and s[-1] == ","


def arrange_foro(s):
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
            foro = strip_first(vda_read[i])
            g = 1
            while circle_line_check(foro):
                foro += strip_next(vda_read[i + g])
                g += 1
            parsed.append(arrange_foro(foro))
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


def report_table(matrix):
    report = 'Trovati i seguenti ' + str(len_matrix(matrix)) + ' fori:\n\n'
    len_x = len_num(matrix, 0)
    len_y = len_num(matrix, 1)
    len_z = len_num(matrix, 2)
    for tabella in matrix:
        report += 'N. {0} fori di diametro {1} mm:\n'.format(str(len(tabella[1])),
                                                             str(tabella[0]))
        for foro in tabella[1]:
            foro_x = arrange_coord(foro[1][0], len_x)
            foro_y = arrange_coord(foro[1][1], len_y)
            foro_z = arrange_coord(foro[1][2], len_z)
            report += '{0}:\tx {1}\t\ty {2}\t\tz {3}\n'.format(str(foro[0]),
                                                               foro_x,
                                                               foro_y,
                                                               foro_z)
        report += '\n'
    return report


def csv_value(value): return str(value).replace('.', csv_conf.d_mark)


def csv_table(matrix):
    csv_export = 'Pos' + csv_conf.separator +\
                 'Ø' + csv_conf.separator +\
                 'X' + csv_conf.separator +\
                 'Y' + csv_conf.separator +\
                 'Z' + '\n'
    for tabella in matrix:
        for foro in tabella[1]:
            csv_export += csv_value(foro[0]) + csv_conf.separator +\
                          csv_value(tabella[0]) + csv_conf.separator +\
                          csv_value(foro[1][0]) + csv_conf.separator +\
                          csv_value(foro[1][1]) + csv_conf.separator +\
                          csv_value(foro[1][2]) + '\n'
    return csv_export


def color(aci): return aci, file_read(workpath + 'aci_colors.kg')[aci][:-1]


def dxf_comment(comment): return '\n999\n' + comment


def dxf_heading(file_name):
    dxf_start = dxf_comment('Hole Table Generator by KG-Soft')[1:]
    dxf_start += dxf_comment('Davide Fasolo 2018')
    dxf_start += dxf_comment('pianta fori da file "' + file_get_full_name(file_name) + '"')
    dxf_start += '\n0\nSECTION\n'
    dxf_start += '2\nENTITIES'
    return dxf_start


def dxf_footer(): return '\n0\nENDSEC\n0\nEOF'


def dxf_level(level): return '\n8\n{0}'.format(level)


def dxf_color(color_aci): return '\n62\n{0}'.format(color_aci)


def dxf_p1(coord): return '\n10\n{0}\n20\n{1}\n30\n{2}'.format(str(coord[0]), str(coord[1]), str(coord[2]))


def dxf_p2(coord): return '\n11\n{0}\n21\n{1}\n31\n{2}'.format(str(coord[0]), str(coord[1]), str(coord[2]))


def dxf_diam(diameter): return '\n40\n{0}'.format(diameter/2)


def dxf_circle(diameter, coord): return '\n0\nCIRCLE{0}{1}{2}{3}'.format(dxf_level(level_conf.circle_level),
                                                                         dxf_p1(coord),
                                                                         dxf_diam(diameter),
                                                                         dxf_color(color_conf.circle_color))


def dxf_axis(coord1, coord2): return '\n0\nLINE{0}{1}{2}{3}'.format(dxf_level(level_conf.axis_level),
                                                                    dxf_p1(coord1),
                                                                    dxf_p2(coord2),
                                                                    dxf_color(color_conf.axis_color))


def dxf_axes(matrix_): return ''.join(list(map(dxf_axis, *min_max(matrix_))))


def rad_ang(angle): return angle * math.pi / 180


def text_width(text): return draw_conf.text_height * draw_conf.font_ratio * len(str(text))


def text_box(text): return [draw_conf.text_height, text_width(text)]


def tag_side(): return draw_conf.text_height * 0.6


def tag_b(text): return max(0.001, 0.35 * (len(str(text))-2.4) * draw_conf.text_height)


def tag_point_matrix(coord, diameter, text):
    p_00 = [coord[0] + diameter / 2 * math.cos(rad_ang(draw_conf.tag_angle)),
           coord[1] + diameter / 2 * math.sin(rad_ang(draw_conf.tag_angle)),
           coord[2]]
    p_01 = [p_00[0] + tag_side() * math.cos(rad_ang(draw_conf.tag_angle)) - tag_side() / 2,
           p_00[1] + tag_side() * math.sin(rad_ang(draw_conf.tag_angle)),
           coord[2]]
    p_02 = [p_01[0] - tag_b(text),
           p_01[1],
           coord[0]]
    p_03 = [p_02[0] - tag_side() * math.sin(math.pi / 4),
           p_02[1] + tag_side() * math.sin(math.pi / 4),
           coord[0]]
    p_04 = [p_03[0],
           p_03[1] + tag_side(),
           coord[0]]
    p_05 = [p_02[0],
           p_04[1] + tag_side() * math.sin(math.pi / 4),
           coord[0]]
    p_06 = [p_01[0] + tag_side() + tag_b(text),
           p_05[1],
           coord[0]]
    p_07 = [p_06[0] + tag_side() * math.sin(math.pi / 4),
           p_04[1],
           coord[0]]
    p_08 = [p_07[0],
           p_03[1],
           coord[0]]
    p_09 = [p_06[0],
           p_01[1],
           coord[0]]
    p_10 = [p_09[0] - tag_b(text),
            p_09[1],
            coord[0]]
    p_tx = [p_01[0] + tag_side() / 2 - text_width(text) / 2,
           p_02[1] * 7 * math.sin(math.pi / 4) / 20,
           coord[0]]
    return [[p_00, p_01, p_02, p_03, p_04, p_05, p_06, p_07, p_08, p_09, p_10], p_tx]


def dxf_polyline_vertex(coord): return '\n0\nVERTEX{0}'.format(dxf_p1(coord))


def dxf_polyline_seq(coord_matrix): return ''.join(list(map(dxf_polyline_vertex, coord_matrix)))


def dxf_tag(point_matrix, text):
    return '\n0\nPOLYLINE{0}{1}\n30\n{3}\n70\n1{2}\n0\nSEQEND'.format(dxf_color(color_conf.tag_color),
                                                                      dxf_level(level_conf.tag_level),
                                                                      dxf_polyline_seq(point_matrix),
                                                                      point_matrix[0][2])


def min_max(matrice):
    min_x = max_x = matrice[0][1][0][1][0] - matrice[0][0] / 2
    min_y = max_y = matrice[0][1][0][1][1] - matrice[0][0] / 2
    for tabella in matrice:
        for foro in tabella[1]:
            min_x = min(min_x, foro[1][0] - tabella[0] / 2)
            max_x = max(max_x, foro[1][0] + tabella[0] / 2)
            min_y = min(min_y, foro[1][1] - tabella[0] / 2)
            max_y = max(max_y, foro[1][1] + tabella[0] / 2)
    return [[min_x, 0, 0], [0, min_y, 0]], [[max_x, 0, 0], [0, max_y, 0]]


def dxf_output(matrice):
    dxf_out = dxf_heading(filename)
    for tabella in matrice:
        dxf_out += dxf_comment('#'*80)
        dxf_out += dxf_comment('N°{0} fori di diametro {1}'.format(str(len(tabella[1])),
                                                                   str(tabella[0])))
        for foro in tabella[1]:
            dxf_out += dxf_comment('#' * 28)
            dxf_out += dxf_comment('foro N°{0} Ø{1}'.format(str(foro[0]),
                                                            str(tabella[0])))
            dxf_out += (dxf_circle(tabella[0], foro[1]))
            dxf_out += dxf_tag(tag_point_matrix(foro[1], tabella[0], foro[0])[0], foro[0])
    dxf_out += dxf_axes(matrice)
    dxf_out += dxf_footer()
    return dxf_out


workpath = os.getcwd() + '\\Configurazione\\'
filename = 'C:\\Users\\Amon\\Documents\\coding\\HTG\\filetestarea\\test.vda'
struct_conf = StructConfig(workpath)
color_conf = ColorConfig(workpath)
level_conf = LevelConfig(workpath)
csv_conf = CsvConfig(workpath)
draw_conf = DrawConfig(workpath)

matrice = hole_matrix(clean_and_sort(parse_vda(file_read(filename))))

print(report_table(matrice))
out_csv = open('C:\\Users\\Amon\\Desktop\\asd.csv', 'w+')
out_csv.write(csv_table(matrice))
out_csv.close()
out_dxf = open('C:\\Users\\Amon\\Desktop\\asd.dxf', 'w+')
out_dxf.write(dxf_output(matrice))
out_dxf.close()


# http://paulbourke.net/dataformats/dxf/
