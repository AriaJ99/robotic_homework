import numpy as np
from math import radians, cos, sin, pi
def rotx(x_ang):
    # function returns a matrix
    # for rotating a vector about the x axis
    rad=radians(x_ang)
    return np.array([[1, 0, 0],
                     [0, cos(rad), -sin(rad)],
                     [0, sin(rad), cos(rad)]])

def roty(y_ang):
    # function returns a matrix
    # for rotating a vector about the y axis
    rad = radian(y_ang)
    return np.array([[cos(rad), 0, sin(rad)],
                     [0, 1, 0],
                     [-sin(rad), 0, cos(rad)]])
def rotz(z_ang):
    # function returns a matrix
    # for rotating a vector about the z axis
    rad = radian(z_ang)
    return np.array([[cos(rad), -sin(rad), 0],
                     [sin(rad), cos(rad), 0],
                     [0, 0, 1]])
