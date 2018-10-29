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


def dxf_heading(filename):
    dxf_start = dxf_comment('Hole Table Generator by KG-Soft')[1:]
    dxf_start += dxf_comment('Davide Fasolo 2018')
    dxf_start += dxf_comment('pianta fori da file "' + file_get_full_name(filename) + '"')
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


def dxf_axes(matrice): return ''.join(list(map(dxf_axis, *min_max(matrice))))


def rad_ang(angle): return angolo * math.pi / 180


def set_tag_start(coord, diameter):
    return [coord[0] + diameter / 2 * math.cos(rad_ang(draw_conf.tag_angle)),
            coord[1] + diameter / 2 * math.sin(rad_ang(draw_conf.tag_angle)),
            coord[2]]


def dxf_tag(coord, diameter):
    p_0 = set_tag_start(coord, diameter)
    


def min_max(matrice):
    min_x = matrice[0][1][0][1][0] - matrice[0][0] / 2
    max_x = matrice[0][1][0][1][0] + matrice[0][0] / 2
    min_y = matrice[0][1][0][1][1] - matrice[0][0] / 2
    max_y = matrice[0][1][0][1][1] + matrice[0][0] / 2
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
    dxf_out += dxf_axes(matrice)
    dxf_out += dxf_footer()
    return dxf_out


workpath = os.getcwd() + '\\Configurazione\\'
filename = 'C:\\drawing\\cad\\tabelle fori XYZ\\Hole Table Generator\\sorgenti\\filetestarea\\test.vda'
struct_conf = StructConfig(workpath)
color_conf = ColorConfig(workpath)
level_conf = LevelConfig(workpath)
csv_conf = CsvConfig(workpath)
draw_conf = DrawConfig(workpath)

matrice = hole_matrix(clean_and_sort(parse_vda(file_read(filename))))

print(report_table(matrice))
out_csv = open('C:\\Users\\davide.fasolo\\Desktop\\asd.csv', 'w+')
out_csv.write(csv_table(matrice))
out_csv.close()
out_dxf = open('C:\\Users\\davide.fasolo\\Desktop\\asd.dxf', 'w+')
out_dxf.write(dxf_output(matrice))
out_dxf.close()
