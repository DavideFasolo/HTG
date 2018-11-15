import os

from infrastructure import *
from outputs import *
from parsers import *


########################################################################################################################


def color(aci): return aci, file_read(workpath + 'aci_colors.kg')[aci][:-1]


########################################################################################################################


workpath = os.getcwd() + '\\Configurazione\\'
filename = os.getcwd() + '\\filetestarea\\test.vda'
try:
    out_dir = (os.getenv('HOME') + '\\Desktop\\').replace('\\', '/')
except TypeError:
    out_dir = (os.getenv('USERPROFILE') + '\\Desktop\\').replace('\\', '/')

dxf_conf = DxfConfig(workpath)
struct_conf = StructConfig(workpath)
csv_conf = CsvConfig(workpath)
ppc_list = Ppcs(workpath)

matrice = build_matrix_vda(filename, struct_conf)

print(report_table(matrice))

selected_tab = 1
z_switch: bool = 'false'

print(cnc_lines(
    matrice, selected_tab, PostProcessor(workpath, ppc_list.plist[1]), z_switch, file_get_full_name(filename)
))
print(cnc_lines(
    matrice, selected_tab, PostProcessor(workpath, ppc_list.plist[0]), z_switch, file_get_full_name(filename)
))

out_selca = open(out_dir + 'FASOLO SELCA.cnc', 'w+')
out_selca.write(cnc_lines(
    matrice, selected_tab, PostProcessor(workpath, ppc_list.plist[0]), z_switch, file_get_full_name(filename)
))
out_selca.close()
out_heiden = open(out_dir + 'FASOLO HEIDENHAIN.h', 'w+')
out_heiden.write(cnc_lines(
    matrice, selected_tab, PostProcessor(workpath, ppc_list.plist[1]), z_switch, file_get_full_name(filename)
))
out_heiden.close()
out_csv = open(out_dir + 'asd.csv', 'w+')
out_csv.write(csv_table(matrice, csv_conf))
out_csv.close()
out_dxf = open(out_dir + 'asd.dxf', 'w+')
out_dxf.write(dxf_structure(matrice, filename, dxf_conf))
out_dxf.close()


from os import listdir
from os.path import isfile, join
onlyfiles = [f.strip('.ppc') for f in listdir(workpath+'ppc\\') if isfile(join(workpath+'ppc\\', f))]
print(onlyfiles)



input()
