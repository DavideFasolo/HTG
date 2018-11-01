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
