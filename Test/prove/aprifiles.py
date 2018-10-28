filename = 'C:/Users/Amon/Documents/coding/HTG/filetestarea/test.vda'


def file_get_full_name(p): return p.split('/').pop()


def file_get_name(f): return file_get_full_name(f).split('.')[0]


def file_get_ext(f): return '.' + file_get_full_name(f).split('.')[1]


def path_add_slash(s): return s + '/'


def path_get_list(p): return p.split('/')[0:-1]


def path_map(p): return map(path_add_slash, path_get_list(p))


def path_get(p): return ''.join(path_map(p)).rstrip('/')


def file_read(file): return open(file, "r").readlines()


def round_value():
    try:
        int(cf.arrot)
    except NameError:
        return 3
    else:
        return int(cf.arrot)


def round_var(v): return round(float(v), round_value())


def circle_check(s):
    return s.count("CIRCLE /" or
                   "CIRCLE/")


def circle_line_check(s):
    return s.count(",") <= 11 and s[-1] == ","


def arrange_foro(s):
    return [round_var(s.split(',')[3]) * 2, list(map(round_var, s.split(',')))[0:-9]]


def strip_first(s):
    return s[s.find("/") + 1:72].strip()


def strip_next(s):
    return s[0:72].strip()


def parse_vda(vda_read):
    vda_read = vda_read[21:-1]
    parsed = list()
    i = 0
    while i < len(vda_read):
        if circle_check(vda_read[i]):
            foro = strip_first(vda_read[i])
            g = 1
            while circle_line_check(foro):
                foro += strip_next(vda_read[i + g])
                g += 1
            parsed.append(arrange_foro(foro))
        i += 1
    return parsed


def clean_and_sort(parsed):
    clean = [x for n, x in enumerate(parsed) if x not in parsed[:n]]
    clean.sort()
    return clean


def hole_matrix(li):
    fori_group = list()
    num_hole = 0
    act_diam = 0
    diam_count = 0
    for something in li:
        if num_hole == 0:
            act_diam = something[0]
            num_hole += 1
            fori_group.append([act_diam, [[num_hole, something[1]]]])
        else:
            if act_diam == something[0]:
                num_hole += 1
                fori_group[diam_count][1].append([num_hole, something[1]])
            else:
                act_diam = something[0]
                num_hole += 1
                fori_group.append([act_diam, [[num_hole, something[1]]]])
                diam_count += 1
    return fori_group


def len_matrix(matrix):
    numero_fori = int()
    for gruppo in matrix:
        numero_fori += len(gruppo[1])
    return numero_fori


def len_num(matrix, c):
    length_a = int()
    length_b = int()
    for tabella in matrix:
        for foro in tabella[1]:
            length_a = max(length_a, len(str(foro[1][c]).split('.')[0]))
            length_b = max(length_b, len(str(foro[1][c]).split('.')[1]))
    return length_a, length_b


def arrange_coord(value, digits):
    value = str(value).split('.')
    if digits[0] > len(value[0]):
        value[0] = ' ' * (digits[0] - len(value[0])) + value[0]
    if digits[1] > len(value[1]):
        value[1] = value[1] + ' ' * (digits[1] - len(value[1]))
    return '.'.join(value)


def report_table(matrix):
    report = 'Trovati i seguenti ' + str(len_matrix(matrix)) + ' fori:\n\n'
    len_x = len_num(matrix, 0)
    len_y = len_num(matrix, 1)
    len_z = len_num(matrix, 2)
    print(len_x)
    for tabella in matrix:
        report += 'N. {0} fori di diametro {1} mm:\n'.format(str(len(tabella[1])),
                                                             str(tabella[0]))
        for foro in tabella[1]:
            foro_x = arrange_coord(foro[1][0], len_x)
            foro_y = arrange_coord(foro[1][1], len_y)
            foro_z = arrange_coord(foro[1][2], len_z)
            report += '{0}:\tx {1}\t\ty {2}\t\tz {3}\n'.format(str(foro[0]),
                                                               foro_x,
                                                               foro_y,
                                                               foro_z)
        report += '\n'
    return report


print(report_table(hole_matrix(clean_and_sort(parse_vda(file_read(filename))))))
