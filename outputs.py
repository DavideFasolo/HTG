from KG_dxf_lib import *
from utilities import *
from itertools import count


#                                                                                                                      _
#                                                CONSOLE OUTPUT                                                        _
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
    csv_export = 'Pos{0}Ø{0}X{0}Y{0}Z\n'.format(csv_config_parser.separator)
    for hole_group in matrix:
        for hole in hole_group[1]:
            csv_export += '{1}{0}{2}{0}{3}{0}{4}{0}{5}\n'.format(csv_config_parser.separator,
                                                                 csv_value(hole[0], csv_config_parser.d_mark),
                                                                 csv_value(hole_group[0], csv_config_parser.d_mark),
                                                                 csv_value(hole[1][0], csv_config_parser.d_mark),
                                                                 csv_value(hole[1][1], csv_config_parser.d_mark),
                                                                 csv_value(hole[1][2], csv_config_parser.d_mark))
    return csv_export


#                                                                                                                      _
#                                               DXF OUTPUT SETUP                                                       _
#                                                                                                                      _


def dxf_out_header_comments(filename_comment):
    return "{0}{1}{2}".format(
        dxf_comment('Hole Table Generator by KG-Soft')[1:],
        dxf_comment('Davide Fasolo 2018'),
        dxf_comment('pianta fori da file "' + filename_comment + '"')
    )


def dxf_out_tables(dxf_config_parser):
    return dxf_section(
        dxf_tables(
            dxf_table(
                dxf_ltype_table(
                    dxf_dash_style(dxf_config_parser.axis_name,
                                   dxf_config_parser.axis_description,
                                   dxf_config_parser.axis_pattern)
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


def dxf_draw_entities(hole_matrix_out, dxf_config_parser):
    dxf_out = str()
    for tabella in hole_matrix_out:
        dxf_out += '{0}{1}'.format(dxf_comment('#'*80),
                                   dxf_comment('N°{0} fori di diametro {1}'.format(str(len(tabella[1])),
                                                                                   str(tabella[0]))))
        for foro in tabella[1]:
            tag_matrix = tag_point_matrix(foro[1], tabella[0], dxf_config_parser.tag_angle, foro[0])
            dxf_out += dxf_comment('#' * 28)
            dxf_out += dxf_comment('foro N°{0} Ø{1}'.format(str(foro[0]),
                                                            str(tabella[0])))
            dxf_out += dxf_circle(tabella[0],
                                  foro[1],
                                  dxf_config_parser.circle_level,
                                  dxf_config_parser.circle_color)
            dxf_out += dxf_polyline(tag_matrix[0],
                                    dxf_config_parser.tag_level,
                                    dxf_config_parser.tag_color)
            dxf_out += dxf_text(foro[0], tag_matrix[1],
                                dxf_config_parser.tag_text_format,
                                dxf_config_parser.text_level,
                                dxf_config_parser.text_color)
    dxf_out += dxf_draw_axes(hole_matrix_out,
                             dxf_config_parser.axis_level,
                             dxf_config_parser.axis_color,
                             dxf_config_parser.axis_name)
    return dxf_section(dxf_entities(dxf_out))


def dxf_structure(entities_matrix, heading_filename, dxf_config_parser):
    return '{0}{1}{2}{3}'.format(dxf_out_header_comments(heading_filename),
                                 dxf_out_tables(dxf_config_parser),
                                 dxf_draw_entities(entities_matrix, dxf_config_parser),
                                 dxf_footer())


#                                                                                                                      _
#                                               CNC OUTPUT SETUP                                                       _
#                                                                                                                      _


def get_table_id(table_matrix):
    return 'Fori diam {0}'.format(table_matrix[0])


def get_table_list(tab_matrix):
    return list(map(get_table_id, tab_matrix))


def cnc_set_z(hole_matrix_tab):
    return get_max_z(hole_matrix_tab) + 100


def cnc_footer(ppc, matrix, tab):
    # {0} = ending program Z
    # {1} = program name
    return ppc.footer.format(ppc.cnc_Zf, get_table_id(matrix[tab]))


def cnc_hole(ppc, tab, z_switch):
    # {0} = end hole Z
    # {1} = drill step: I
    # {2} = start hole Z: J
    # {3} = rapid movement Z: Q
    # {4}{5} = XY coordinates
    # {6} = line comment hole table reference
    return ppc.hole_line.format(ppc.cnc_Z,
                                ppc.cnc_I,
                                (z_switch == 'true' and tab[1][2]) or ppc.cnc_J,
                                ppc.cnc_Q,
                                tab[1][0],
                                tab[1][1],
                                ppc.com_hole.format(tab[0]))


def z_header_true(ppc, filename, matrix, tab):
    return ppc.z_true.format(filename,
                             len(matrix[tab][1]),
                             get_table_id(matrix[tab]))


def cnc_header(ppc, z_switch, matrix, tab, filename):
    # {0} = Drilling Feed: F
    # {1} = Drilling rpm: S
    # {2} = Hole group name
    # {3} = full vda path and name
    # {4} = number of holes in the group
    # {5} = header section if z-coord is true
    return ppc.header.format(ppc.cnc_F,
                             ppc.cnc_S,
                             get_table_id(matrix[tab]),
                             filename,
                             len(matrix[tab][1]),
                             (not z_switch == 'true' and z_header_true(ppc, filename, matrix, tab)) or '')


def hole_cnc_build(ppc, hole_list, z_switch):
    return '\n{0} {1}'.format(cnc_hole(ppc, hole_list, z_switch),
                              ppc.endline.format(hole_list[0]))


def cnc_list_hole(ppc, hole_list, z_switch):
    return '{0} {1}'.format(
        ''.join(list(map(hole_cnc_build, cycle([ppc]), hole_list, cycle([z_switch])))).strip(
            ppc.endline.format(hole_list[-1][0])),
        ppc.lastline.format(hole_list[-1][0]))


def cnc_build(matrix, tab, ppc, z_switch, filename):
    return '{3}{0}{1}\n{2}'.format(
        cnc_header(ppc, z_switch, matrix, tab, filename),
        cnc_list_hole(ppc, matrix[tab][1], z_switch),
        cnc_footer(ppc, matrix, tab),
        ppc.com_header.format(get_table_id(matrix[tab]))).split('\n')


def cnc_lines(matrix, tab, ppc, z_switch, filename):
    return ''.join(list(map(lambda line, line_id, line_number, separ: '{0}{1}{3}{2}\n'.format(
        line_id, line_number, line, separ),
                            cnc_build(matrix, tab, ppc, z_switch, filename),
                            ppc.line_nums == 'true' and cycle([ppc.line_id]) or cycle(['']),
                            ppc.line_nums == 'true' and count(ppc.line_start, ppc.line_step) or cycle(['']),
                            cycle([ppc.separator]))))
