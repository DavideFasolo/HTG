import os

from infrastructure import *
from outputs import *
from parsers import *


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
    return '\n[\n[foro N°{1}\n[\n{0}'.format(ppc.hole_line.format('P43',
                                                                  'P42',
                                                                  hole_list[1][2],
                                                                  'P44',
                                                                  hole_list[1][0],
                                                                  hole_list[1][1]),
                                             hole_list[0])


def cnc_list_hole(ppc, matrix, hole_list):
    return ''.join(list(map(hole_cnc_build, cycle([ppc]), hole_list, cycle([max(get_max_z(matrix) + 100, ppc.zsec)]))))


def cnc_build(matrix, tab, ppc):
    return '[\n[FORI Ø{3}\n[\n[----------\n[\n{0}{1}{2}'.format(ppc.header.format('P41', 'P40'),
                                                                cnc_list_hole(ppc, matrix, matrix[tab][1]),
                                                                ppc.footer.format(ppc.zfin),
                                                                matrix[tab][0]).split('\n')


pippo = cnc_build(matrice, selected_tab, PostProcessor(workpath, selected_ppc))
ciccio = str()

for (number, line) in enumerate(pippo, 1):
    ciccio += 'N\t{0}\t\t{1}\n'.format(number, line)

print(ciccio)


# print(report_table(matrice))


# out_csv = open('C:\\Users\\Amon\\Desktop\\asd.csv', 'w+')
# out_csv.write(csv_table(matrice, csv_conf))
# out_csv.close()
# out_dxf = open('C:\\Users\\Amon\\Desktop\\asd.dxf', 'w+')
# out_dxf.write(dxf_structure(matrice, filename, dxf_conf))
# out_dxf.close()

# http://paulbourke.net/dataformats/dxf/
