from math import sqrt, sin, cos
from random import randint

def add2D(a, b):
    return [a[0]+b[0],a[1]+b[1]]

def subtract2D(a, b):
    return [a[0]-b[0],a[1]-b[1]]

def multiply2D(a, b):
    return [a[0]*b[0],a[1]*b[1]]
    
def divide2D(a, b):
    return [a[0]/b[0],a[1]/b[1]]



def clamp2D(p, minimum, maximum):
    return [clamp1D(p[0], minimum[0], maximum[0]), clamp1D(p[1], minimum[1], maximum[1])]

def clamp1D(p, minimum, maximum):
    return min(maximum, max(minimum, p))

def max2D(p, maximum):
    return [max(p[0], maximum[0]), max(p[1], maximum[1])]

def min2D(p, maximum):
    return [min(p[0], maximum[0]), min(p[1], maximum[1])]


def hypotenuse2D(a, b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


def random_unit_vector():
    angle = randint(0,360)
    return [cos(angle), sin(angle)]


def get_movement_direction(direction):
    direction %= 4
    if direction == 0:
        return [0,-1]
    elif direction == 1:
        return [1,0]
    elif direction == 2:
        return [0,1]
    elif direction == 3:
        return [-1,0]
    else:
        return [0,0] # just in case

def adjacent(a, b):
    # checks if a and b are horizontally or vertically adjacent (not diagonally)
    for i in range(4):
        direction = get_movement_direction(i)
        if add2D(a, direction) == b:
            return True
    return False


def random2D(x, y):
    return [randint(x[0], x[1]), randint(y[0], y[1])]