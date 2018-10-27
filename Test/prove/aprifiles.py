filename = 'C:/Users/Amon/Documents/coding/HTG/filetestarea/test.vda'


def file_get_full_name(p): return p.split('/').pop()


def file_get_name(f): return file_get_full_name(f).split('.')[0]


def file_get_ext(f): return '.' + file_get_full_name(f).split('.')[1]


def path_add_slash(s): return s + '/'


def path_get_list(p): return p.split('/')[0:-1]


def path_map(p): return map(path_add_slash, path_get_list(p))


def path_get(p): return ''.join(path_map(p)).rstrip('/')


def file_read(f): return open(f, "r").readlines()[21:-1]


def round_value():
    try:
        int(cf.arrot)
    except NameError:
        return 3
    else:
        return int(cf.arrot)


def round_var(v): return round(float(v), round_value())


def matrix_def(text):
    fori = list()
    i = 0
    while i < len(text):
        if text[i].count("CIRCLE /") + text[i].count("CIRCLE/"):
            foro = text[i][text[i].find("/")+1:72].strip()
            g = 1
            while foro.count(",") <= 11 and foro[len(foro) - 1] == ",":
                foro += text[i + g][0:72].strip()
                g += 1
            foro = [round_var(foro.split(',')[3])*2, list(map(round_var, foro.split(',')))[0:-9]]
            fori.append(foro)
        i += 1
    fori = [x for n, x in enumerate(fori) if x not in fori[:n]]
    fori.sort()
    return fori


pippo = matrix_def(file_read(filename))
i = 0
for item in pippo:
    print(str(pippo[i][0]) + ' \t' + '  \t      \t  '.join(str(pippo[i][1]).strip('[]').split(',')))
    i += 1
# print(matrix_def(file_read(filename)))

#print(''.join(ciccio))

#    in_file.close()
# print(path_get(filename))
# print(file_get_name(filename))
# print(file_get_ext(filename))


