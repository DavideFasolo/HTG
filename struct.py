import os

from infrastructure import *
from outputs import *
from parsers import *
from itertools import count


########################################################################################################################


def color(aci): return aci, file_read(workpath + 'aci_colors.kg')[aci][:-1]


########################################################################################################################


workpath = os.getcwd() + '\\Configurazione\\'
filename = os.getcwd() + '\\filetestarea\\test.vda'
dxf_conf = DxfConfig(workpath)
struct_conf = StructConfig(workpath)
csv_conf = CsvConfig(workpath)
ppc_list = Ppcs(workpath)

matrice = build_matrix_vda(filename, struct_conf)

selected_ppc = ppc_list.plist[0]
selected_tab = 3


def get_table_id(table_matrix):
    return 'Fori Ø{0}'.format(table_matrix[0])


def get_table_list(tab_matrix):
    return list(map(get_table_id, tab_matrix))


def cnc_set_z(hole_matrix_tab):
    return get_max_z(hole_matrix_tab) + 100


def hole_cnc_build(ppc, hole_list, zsec):
    return '{1}\n{0}'.format(ppc.hole_line.format('P43',
                                                  'P42',
                                                  hole_list[1][2],
                                                  'P44',
                                                  hole_list[1][0],
                                                  hole_list[1][1]),
                             ppc.com_hole.format(hole_list[0])
                             )


def cnc_list_hole(ppc, matrix, hole_list):
    return ''.join(list(map(hole_cnc_build, cycle([ppc]), hole_list, cycle([max(get_max_z(matrix) + 100, ppc.zsec)]))))


def cnc_build(matrix, tab, ppc):
    return '{3}{0}{1}\n{2}'.format(ppc.header.format('P41', 'P40', get_table_id(matrix[tab])),
                                                                cnc_list_hole(ppc, matrix, matrix[tab][1]),
                                                                ppc.footer.format(ppc.zfin,'',get_table_id(matrix[tab])),
                                                                ppc.com_header.format(get_table_id(matrix[tab]))).split('\n')


def cnc_selca(matrix, tab, ppc):
    return ''.join(list(map(lambda number, line, lin_id: '{2}{0}{1}\n'.format(number, line, lin_id),
                            ppc.line_nums == 'true' and count(ppc.line_start, ppc.line_step) or cycle(['']),
                            cnc_build(matrix, tab, ppc),
                            ppc.line_nums == 'true' and cycle([ppc.line_id]) or cycle([''])
                            )))


pippo = cnc_selca(matrice, selected_tab, PostProcessor(workpath, selected_ppc))

print(pippo)


# print(report_table(matrice))


# out_csv = open('C:\\Users\\Amon\\Desktop\\asd.csv', 'w+')
# out_csv.write(csv_table(matrice, csv_conf))
# out_csv.close()
# out_dxf = open('C:\\Users\\Amon\\Desktop\\asd.dxf', 'w+')
# out_dxf.write(dxf_structure(matrice, filename, dxf_conf))
# out_dxf.close()

# http://paulbourke.net/dataformats/dxf/
