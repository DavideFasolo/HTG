filename = 'C:/drawing/cad/tabelle fori XYZ/Hole Table Generator/sorgenti/filetestarea/test.vda'
p = str()
print(filename.split('/'))


def add_slash(s): return str(s) + '/'


def concat(s): p += s


def set_p(p):
    list(map(add_slash, filename.split('/')))

#        for e in lst:  func(e)
#        map(func,lst)


map(concat, list(map(add_slash, filename.split('/'))))
print(p)

