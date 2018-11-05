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


def cnc_build(ppc: PostProcessor):
    cnc_out = '{0}\n{1}\n{2}'.format(ppc.header.format(ppc.feed,
                                                       ppc.srpm),
                                     ppc.hole_line.format(ppc.zend,
                                                          ppc.step,
                                                          -12.35,
                                                          ppc.zsec,
                                                          23.56, 15.33,),
                                     ppc.footer.format(ppc.zfin))
    return cnc_out


def hole_cnc_build(ppc):
    return '\n{0}'.format(ppc.hole_line.format(ppc.zend,
                                               ppc.step,
                                               -12.35,
                                               ppc.zsec,
                                               23.56, 15.33,))


pippo = list(map(hole_cnc_build, cycle([PostProcessor(workpath, selected_ppc)]), matrice[0][1][1]))


print(pippo)

# print(report_table(matrice))


# out_csv = open('C:\\Users\\Amon\\Desktop\\asd.csv', 'w+')
# out_csv.write(csv_table(matrice, csv_conf))
# out_csv.close()
# out_dxf = open('C:\\Users\\Amon\\Desktop\\asd.dxf', 'w+')
# out_dxf.write(dxf_structure(matrice, filename, dxf_conf))
# out_dxf.close()

# http://paulbourke.net/dataformats/dxf/
