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


pippo = [
    [
        6.0,
        [
            [1, [-51.655, 83.781, -15.777]],
            [2, [-33.943, 83.781, -3.655]],
            [3, [33.277, 83.781, -3.655]],
            [4, [50.989, 83.781, -15.777]]
        ]
    ],
    [
        8.0,
        [
            [5, [-131.855, 0.366, -19.547]],
            [6, [-131.855, 83.781, -16.537]],
            [7, [131.195, 0.366, -19.547]],
            [8, [131.195, 83.781, -16.537]]
        ]
    ],
    [
        10.0,
        [
            [9, [-20.0, 0.0, -87.235]],
            [10, [0.0, -22.0, -87.235]],
            [11, [0.0, 22.0, -87.235]],
            [12, [20.0, 0.0, -87.235]]
        ]
    ],
    [
        12.0,
        [
            [13, [-131.855, 30.366, -12.363]],
            [14, [-129.32, -81.337, -32.463]],
            [15, [-117.992, 125.227, -5.859]],
            [16, [-115.809, -131.312, -12.363]],
            [17, [-41.855, -134.634, -12.363]],
            [18, [-21.855, 126.366, 9.347]],
            [19, [44.403, -134.611, -25.428]],
            [20, [77.802, 126.768, -12.363]],
            [21, [131.189, -134.634, 0.2]],
            [22, [131.189, -54.634, -12.363]],
            [23, [131.189, 40.366, -12.363]],
            [24, [131.189, 126.366, -6.333]]
        ]
    ],
    [
        16.0,
        [
            [25, [-125.0, -200.0, 0.0]],
            [26, [-125.0, 200.0, 0.0]],
            [27, [125.0, -200.0, 0.0]],
            [28, [125.0, 200.0, 0.0]]
        ]
    ]
]
print('X min = ' + str(get_min_x(pippo)))
print('X max = ' + str(get_max_x(pippo)))
print('Y min = ' + str(get_min_y(pippo)))
print('Y max = ' + str(get_max_y(pippo)))
print('Z min = ' + str(get_min_z(pippo)))
print('Z max = ' + str(get_max_z(pippo)))
