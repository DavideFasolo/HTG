import os

from infrastructure import *
from outputs import *
from parsers import *


########################################################################################################################


def color(aci): return aci, file_read(workpath + 'aci_colors.kg')[aci][:-1]


########################################################################################################################


workpath = os.getcwd() + '\\Configurazione\\'
filename = 'C:\\Users\\Amon\Documents\\coding\\HTG\\filetestarea\\test.vda'
dxf_conf = DxfConfig(workpath)
struct_conf = StructConfig(workpath)
csv_conf = CsvConfig(workpath)

matrice = build_matrix_vda(filename, struct_conf)


print(report_table(matrice))


out_csv = open('C:\\Users\\Amon\\Desktop\\asd.csv', 'w+')
out_csv.write(csv_table(matrice, csv_conf))
out_csv.close()
out_dxf = open('C:\\Users\\Amon\\Desktop\\asd.dxf', 'w+')
out_dxf.write(dxf_structure(matrice, filename, dxf_conf))
out_dxf.close()

# http://paulbourke.net/dataformats/dxf/
