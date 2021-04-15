from numpy import matrix as np_matrix
from math import sin, cos, tan, sqrt

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

def rotate_point_3d(point, rotation_matrix):
    '''
    Returns the 3D point rotated around the origin, using the supplied rotation matrix.
    '''

    return rotation_matrix * np_matrix(
        [
            [point[0]],
            [point[1]],
            [point[2]]
        ]
    )

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

    rotate_x = np_matrix(
        [
            [1, 0, 0],
            [0, c_ax, s_ax],
            [0, -s_ax, c_ax]
        ]
    )
    
    rotate_y = np_matrix(
        [
            [c_ay, 0, -s_ay],
            [0, 1, 0],
            [s_ay, 0, c_ay]
        ]
    )
    
    rotate_z = np_matrix(
        [
            [c_az, s_az, 0],
            [-s_az, c_az, 0],
            [0, 0, 1]
        ]
    )

    return rotate_x * rotate_y * rotate_z

def get_distance_3d(a, b):
    '''
    Returns the distance from 3D point A to 3D point B.
    '''
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)