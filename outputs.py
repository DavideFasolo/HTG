from KG_dxf_lib import *
from utilities import *


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
