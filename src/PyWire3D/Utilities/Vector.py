from numpy import matmul as np_matmul
from math import sin, cos, tan

def add(*args):
    '''
    Returns the result of the lists being added together item by item. Every list supplied must be the same length.
    '''

    if len(args) == 0:
        return []

    length = len(args[0])
    total = [0] * length

    for arg in args:
        if len(arg) != length:
            raise ValueError('Every list supplied must be the same length.')

        for i, item in enumerate(arg):
            total[i] += item

    return total

def add_3d(a, b):
    '''
    A faster version of add, without sanity checks, only for two lists of length 3.
    '''
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def scale_3d(a, b):
    return [a[0] * b, a[1] * b, a[2] * b]

def clamp_3d(a, bounds):
    return [clamp_1d(a[0], bounds), clamp_1d(a[1], bounds), clamp_1d(a[2], bounds)]

def clamp_1d(a, bounds):
    return max(bounds[0], min(bounds[1], a))

# def rotate_point_3d(point, rotation_matrix):
#     '''
#     Returns the 3D point rotated around the origin, using the supplied rotation matrix.
#     Obsolete: use numpy.matmul(rotation_matrix, point)
#     '''

#     return rotation_matrix * np_matrix(
#         [
#             [point[0]],
#             [point[1]],
#             [point[2]]
#         ]
#     )

def matrix_to_list_3d(matrix):
    return [matrix.item(0), matrix.item(1), matrix.item(2)]

# def get_rotation_matrix_3d(angle):
#     '''
#     Returns the 3D rotation matrix for the angle [x, y, z].
#     Each angle represents a rotation around the corresponding axis.
#     '''

#     s_ax = sin(angle[0])
#     c_ax = cos(angle[0])

#     s_ay = sin(angle[1])
#     c_ay = cos(angle[1])

#     s_az = sin(angle[2])
#     c_az = cos(angle[2])

#     rotate_x = np_matrix(
#         [
#             [1, 0, 0],
#             [0, c_ax, s_ax],
#             [0, -s_ax, c_ax]
#         ]
#     )
    
#     rotate_y = np_matrix(
#         [
#             [c_ay, 0, -s_ay],
#             [0, 1, 0],
#             [s_ay, 0, c_ay]
#         ]
#     )
    
#     rotate_z = np_matrix(
#         [
#             [c_az, s_az, 0],
#             [-s_az, c_az, 0],
#             [0, 0, 1]
#         ]
#     )

#     return rotate_x * rotate_y * rotate_z

def get_rotation_matrix_3d(angle):
    '''
    Returns the 3D rotation matrix for the angle [x, y, z].
    Each angle represents a rotation around the corresponding axis.
    '''

    s_ax = sin(angle[0])
    c_ax = cos(angle[0])

    s_ay = sin(angle[1])
    c_ay = cos(angle[1])

    s_az = sin(angle[2])
    c_az = cos(angle[2])

    return np_matmul(
        np_matmul(
            [
                [1, 0, 0],
                [0, c_ax, s_ax],
                [0, -s_ax, c_ax]
            ],
            [
                [c_ay, 0, -s_ay],
                [0, 1, 0],
                [s_ay, 0, c_ay]
            ]
        ),
        [
            [c_az, s_az, 0],
            [-s_az, c_az, 0],
            [0, 0, 1]
        ]
    )

# def get_rotation_matrix_3d_x(x):
#     '''
#     Returns the 3D rotation matrix for the angle x (a rotation around the x axis).
#     '''
#     s_ax = sin(x)
#     c_ax = cos(x)

#     return np_matrix(
#         [
#             [1, 0, 0],
#             [0, c_ax, s_ax],
#             [0, -s_ax, c_ax]
#         ]
#     )
    
# def get_rotation_matrix_3d_y(y):
#     '''
#     Returns the 3D rotation matrix for the angle y (a rotation around the y axis).
#     '''
#     s_ay = sin(y)
#     c_ay = cos(y)

#     return np_matrix(
#         [
#             [c_ay, 0, -s_ay],
#             [0, 1, 0],
#             [s_ay, 0, c_ay]
#         ]
#     )
    
# def get_rotation_matrix_3d_z(z):
#     '''
#     Returns the 3D rotation matrix for the angle z (a rotation around the z axis).
#     '''
#     s_az = sin(z)
#     c_az = cos(z)

#     return np_matrix(
#         [
#             [c_az, s_az, 0],
#             [-s_az, c_az, 0],
#             [0, 0, 1]
#         ]
#     )

def get_rotation_matrix_3d_x(x):
    '''
    Returns the 3D rotation matrix for the angle x (a rotation around the x axis).
    '''
    s_ax = sin(x)
    c_ax = cos(x)

    return [
            [1, 0, 0],
            [0, c_ax, s_ax],
            [0, -s_ax, c_ax]
        ]
    
def get_rotation_matrix_3d_y(y):
    '''
    Returns the 3D rotation matrix for the angle y (a rotation around the y axis).
    '''
    s_ay = sin(y)
    c_ay = cos(y)

    return [
            [c_ay, 0, -s_ay],
            [0, 1, 0],
            [s_ay, 0, c_ay]
        ]
    
def get_rotation_matrix_3d_z(z):
    '''
    Returns the 3D rotation matrix for the angle z (a rotation around the z axis).
    '''
    s_az = sin(z)
    c_az = cos(z)

    return [
            [c_az, s_az, 0],
            [-s_az, c_az, 0],
            [0, 0, 1]
        ]

def get_square_distance_3d(a, b):
    '''
    Returns the square of the distance from 3D point A to 3D point B.
    '''
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

def get_sum_square_distance_3d(p, a, b, c):
    return get_square_distance_3d(p, a) + get_square_distance_3d(p, b) + get_square_distance_3d(p, c)