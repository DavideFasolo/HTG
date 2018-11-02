from itertools import repeat


#                                                                                                                      _
#                                                       FILE                                                           _
#                                                                                                                      _


def file_get_full_name(p):
    return p.split('/').pop()


def file_get_name(f):
    return file_get_full_name(f).split('.')[0]


def file_get_ext(f):
    return '.' + file_get_full_name(f).split('.')[1]


def path_map(p):
    return map(lambda s: '{0}/'.format(s), p.split('/')[0:-1])


def path_get(p):
    return ''.join(path_map(p)).rstrip('/')


def file_read(file):
    return open(file, "r").readlines()


#                                                                                                                      _
#                                                  PARSER VDA                                                          _
#                                                                                                                      _


def round_value(struct_config_parser):
    try:
        int(struct_config_parser.round_val)
    except NameError:
        print('Valore di approssimazione non trovato')
        print('verrà usato un default di 3 cifre decimali')
        return 3
    else:
        return int(struct_config_parser.round_val)


def round_var(v, struct_config_parser): return round(float(v), struct_config_parser.round_val)


def circle_check(s):
    return s.count("CIRCLE /" or
                   "CIRCLE/")


def circle_line_check(s):
    return s.count(",") <= 11 and s[-1] == ","


def arrange_hole(s, struct_config_parser):
    return [
        round_var(s.split(',')[3], struct_config_parser) * 2,
        list(map(round_var, s.split(','), repeat(struct_config_parser)))[0:-9]
    ]


def strip_first(s):
    return s[s.find("/") + 1:72].strip()


def strip_next(s):
    return s[0:72].strip()


def parse_vda(vda_read, struct_config_parser):
    vda_read = vda_read[21:-1]
    parsed = list()
    i = 0
    while i < len(vda_read):
        if circle_check(vda_read[i]):
            hole = strip_first(vda_read[i])
            g = 1
            while circle_line_check(hole):
                hole += strip_next(vda_read[i + g])
                g += 1
            parsed.append(arrange_hole(hole, struct_config_parser))
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


def build_matrix_vda(file_path, struct_config_parser):
    return hole_matrix(clean_and_sort(parse_vda(file_read(file_path), struct_config_parser)))
