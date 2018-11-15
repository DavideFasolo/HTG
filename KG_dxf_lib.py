import math
from itertools import cycle


#                                                                                                                      _
#                                                    COMMON BLOCKS                                                     _
#                                                                                                                      _


def dxf_comment(comment): return '\n999\n' + comment


def dxf_section(section_content):
    return '\n0\nSECTION{0}\n0\nENDSEC'.format(section_content)


def dxf_entities(entities_content):
    return '\n2\nENTITIES{0}'.format(entities_content)


def dxf_tables(tables_content):
    return '\n2\nTABLES{0}\n0\nENDTAB'.format(tables_content)


def dxf_table(table_content):
    return '\n0\nTABLE{0}'.format(table_content)


def dxf_ltype_table(ltype_table_content):
    return dxf_table('\n2\nLTYPE{0}'.format(ltype_table_content))


def dxf_style_table(style_table_content):
    return dxf_table('\n2\nSTYLE{0}'.format(style_table_content))


def dxf_ltype(ltype_content):
    return '\n0\nLTYPE{0}'.format(ltype_content)


def dxf_style(style_name, style_font):
    return '\n0\nSTYLE\n{0}\n3\n{1}'.format(style_name, style_font)


def entity_style(stylename):
    return '\n6\n{0}'.format(stylename)


def dxf_footer():
    return '\n0\nEOF'


def dxf_level(level):
    return '\n8\n{0}'.format(level)


def dxf_color(color_aci: int):
    return '\n62\n{0}'.format(color_aci)


def dxf_diam(diameter: float):
    return '\n40\n{0}'.format(diameter/2)


def dxf_text_value(text_value):
    return '\n1\n{0}'.format(text_value)


def dxf_text_stylename(text_stylename):
    return '\n7\n{0}'.format(text_stylename)


def dxf_p1(coord: list):
    # <coord> must be a list containing x/y/z coordinates:          #
    #   [ x1 , y1 , z1 ]                                            #
    return '\n10\n{0}\n20\n{1}\n30\n{2}'.format(str(coord[0]), str(coord[1]), str(coord[2]))


def dxf_p2(coord: list):
    # <coord> must be a list containing x/y/z coordinates:          #
    #   [ x2 , y2 , z2 ]                                            #
    return '\n11\n{0}\n21\n{1}\n31\n{2}'.format(str(coord[0]), str(coord[1]), str(coord[2]))


def dxf_vertex_sequence(coord: list):
    # <coord> must be a list containing x/y/z coordinates lists for n points, for example:          #
    #   [ [ x1 , y1 , z1 ] , [ x2 , y2 , z2 ] , [ xn , yn , zn ] ]                                  #
    return '\n0\nVERTEX{0}'.format(dxf_p1(coord))


#                                                                                                                      _
#                                                     DASH STYLE                                                       _
#                                                                                                                      _

# the <pattern> value must be a list containing       #
# length values of dashes and spaces between them:    #
#                                                     #
#       ---   ----- -----       ---                   #
#      [ 3  3   5  1  5     7    3 ]                  #
#                                                     #

def dxf_dashes(pattern: list):
    return '\n73\n{2}\n40\n{0}{1}'.format(
        sum(pattern),
        ''.join(list(map(lambda dash, sign: '\n49\n{0}{1}'.format(sign, dash), pattern, cycle(['', '-'])))),
        len(pattern))


def dxf_dash_style(ds_name, ds_descr, pattern):
    return dxf_ltype('\n2\n{0}\n3\n{1}\n72\n65{2}'.format(ds_name,
                                                          ds_descr,
                                                          dxf_dashes(pattern)))


#                                                                                                                      _
#                                                       CIRCLE                                                         _
#                                                                                                                      _


def dxf_circle(circle_diameter, center_coord, circle_level, circle_color):
    return '\n0\nCIRCLE{0}{1}{2}{3}'.format(
        dxf_level(circle_level),
        dxf_p1(center_coord),
        dxf_diam(circle_diameter),
        dxf_color(circle_color))


#                                                                                                                      _
#                                                       TEXT                                                           _
#                                                                                                                      _


def dxf_text_format(format_code: list):
    # <format_code> is a list containing 4 values representing respectively:            #
    # 1:    horizontal alignment    (0 = left, 1 = center, 2 = right)                   #
    # 2:    vertical alignment      (0 = baseline, 1= bottom, 2 = middle, 3 = top       #
    # 3:    font size (height)                                                          #
    # 3:    font size (width restrain)                                                  #
    return'\n72\n{0}\n73\n{1}\n40\n{2}\n41\n{3}'.format(format_code[0],
                                                        format_code[1],
                                                        format_code[2],
                                                        format_code[3])


def dxf_text(text_value, text_coord: list, text_format: list, text_stylename, text_level, text_color):
    return '\n0\nTEXT{0}{1}{2}{3}{4}{5}{6}'.format(
        dxf_level(text_level),
        dxf_text_format(text_format),
        dxf_p2(text_coord),
        dxf_color(text_color),
        dxf_p1(text_coord),
        dxf_text_value(text_value),
        dxf_text_stylename(text_stylename)
    )


#                                                                                                                      _
#                                                  LINE - POLYLINE                                                     _
#                                                                                                                      _


def dxf_polyline(polyline_point_matrix: list, polyline_level, polyline_color):
    return '\n0\nPOLYLINE{0}{1}\n30\n{2}\n70\n1{3}\n0\nSEQEND'.format(dxf_color(polyline_color),
                                                                      dxf_level(polyline_level),
                                                                      polyline_point_matrix[0][2],
                                                                      ''.join(list(map(dxf_vertex_sequence,
                                                                                       polyline_point_matrix))))


def dxf_line(coord1: list, coord2: list, line_level, line_color, line_style):
    return '\n0\nLINE{4}{0}{1}{2}{3}'.format(dxf_level(line_level),
                                             dxf_p1(coord1),
                                             dxf_p2(coord2),
                                             dxf_color(line_color),
                                             entity_style(line_style))


#                                                                                                                      _
#                                                       TAG                                                            _
#                                                                                                                      _


def rad_ang(angle):
    return angle * math.pi / 180


def tag_side(text_height): return text_height * 0.6


def tag_b(text, text_height, font_ratio):
    return max(0.001, font_ratio / 3.5 * (len(str(text))-font_ratio) * text_height)


def tag_point_matrix(coord, diameter, angle, text, text_height=3.5, font_ratio=0.95):
    p_00 = [coord[0] + diameter / 2 * math.cos(rad_ang(angle)),
            coord[1] + diameter / 2 * math.sin(rad_ang(angle)),
            coord[2]]
    p_01 = [p_00[0] + tag_side(text_height) * math.cos(rad_ang(angle)) - tag_side(text_height) / 2,
            p_00[1] + tag_side(text_height) * math.sin(rad_ang(angle)),
            coord[2]]
    p_02 = [p_01[0] - tag_b(text, text_height, font_ratio),
            p_01[1],
            coord[2]]
    p_03 = [p_02[0] - tag_side(text_height) * math.sin(math.pi / 4),
            p_02[1] + tag_side(text_height) * math.sin(math.pi / 4),
            coord[2]]
    p_04 = [p_03[0],
            p_03[1] + tag_side(text_height),
            coord[2]]
    p_05 = [p_02[0],
            p_04[1] + tag_side(text_height) * math.sin(math.pi / 4),
            coord[2]]
    p_06 = [p_01[0] + tag_side(text_height) + tag_b(text, text_height, font_ratio),
            p_05[1],
            coord[2]]
    p_07 = [p_06[0] + tag_side(text_height) * math.sin(math.pi / 4),
            p_04[1],
            coord[2]]
    p_08 = [p_07[0],
            p_03[1],
            coord[2]]
    p_09 = [p_06[0],
            p_01[1],
            coord[2]]
    p_10 = [p_09[0] - tag_b(text, text_height, font_ratio),
            p_09[1],
            coord[2]]
    p_tx = [p_01[0] + tag_side(text_height) / 2,
            p_01[1] + (p_05[1] - p_01[1]) / 2,
            coord[2]]
    return [[p_00, p_01, p_02, p_03, p_04, p_05, p_06, p_07, p_08, p_09, p_10], p_tx]
