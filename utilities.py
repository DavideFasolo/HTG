#                                                                                                                      _
#                                                   UTILITY                                                            _
#                                                                                                                      _


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


##


def proc_tables(matrix):
    return matrix[1]


def proc_holes(matrix):
    return list(map(proc_tables, matrix))


def proc_x(matrix):
    return matrix[0]


def proc_y(matrix):
    return matrix[1]


def proc_z(matrix):
    return matrix[2]


def proc_hole_x(matrix):
    return list(map(proc_x, matrix))


def proc_hole_y(matrix):
    return list(map(proc_y, matrix))


def proc_hole_z(matrix):
    return list(map(proc_z, matrix))


def get_min_x(matrix):
    return min(list(map(min, list(map(proc_hole_x, list(map(proc_holes, proc_holes(matrix))))))))


def get_max_x(matrix):
    return max(list(map(max, list(map(proc_hole_x, list(map(proc_holes, proc_holes(matrix))))))))


def get_min_y(matrix):
    return min(list(map(min, list(map(proc_hole_y, list(map(proc_holes, proc_holes(matrix))))))))


def get_max_y(matrix):
    return max(list(map(max, list(map(proc_hole_y, list(map(proc_holes, proc_holes(matrix))))))))


def get_min_z(matrix):
    return min(list(map(min, list(map(proc_hole_z, list(map(proc_holes, proc_holes(matrix))))))))


def get_max_z(matrix):
    return max(list(map(max, list(map(proc_hole_z, list(map(proc_holes, proc_holes(matrix))))))))


def min_max(min_max_matrix):
    return [
               [get_min_x(min_max_matrix), 0, 0],
               [0, get_min_y(min_max_matrix), 0]
           ], [
               [get_max_x(min_max_matrix), 0, 0],
               [0, get_max_y(min_max_matrix), 0]]
