filename = 'C:/drawing/cad/tabelle fori XYZ/Hole Table Generator/sorgenti/filetestarea/test.vda'


def file_get_full_name(p): return p.split('/').pop()


def file_get_name(f): return (file_get_full_name(f).split('.')[0])


def file_get_ext(f): return '.' + file_get_full_name(f).split('.')[1]


def path_add_slash(s): return s + '/'


def path_get_list(p): return p.split('/')[0:-1]


def path_map(p): return map(path_add_slash, path_get_list(p))


def path_get(p): return ''.join(path_map(p)).rstrip('/')


def file_read(f): return open(f, "r").readlines()[21:-1]


def line_select(line):
    return (line.count("CIRCLE /") or line.count("CIRCLE/")) and line[0:72].strip()


def line_map(f): return list(map(line_select, file_read(f)))

line = 't,r,f,g,h,j,k,n,b,t,'
(line.count(",") <= 11 and line[-1:] == ',')
#    in_file.close()
# print(path_get(filename))
# print(file_get_name(filename))
# print(file_get_ext(filename))
print((line.count(",") <= 11 and line[-1:] == ','))

