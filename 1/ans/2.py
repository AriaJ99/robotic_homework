import numpy as np
from math import radians, cos, sin, pi
def eul2r(alpha,beta,gamma):
    # function returns a matrix that can be used as eulers rotation matrix zyz
    a_rad=radians(alpha)
    b_rad=radians(beta)
    g_rad=radians(gamma)
    r1=cos(a_rad)*cos(b_rad)*cos(g_rad)-sin(a_rad)*sin(g_rad)
    r2=-cos(a_rad)*cos(b_rad)*sin(g_rad)-sin(a_rad)*cos(g_rad)
    r3=cos(a_rad)*sin(b_rad)
    r4=sin(a_rad)*cos(b_rad)*cos(g_rad)+cos(a_rad)*sin(g_rad)
    r5=-sin(a_rad)*cos(b_rad)*cos(g_rad)+cos(a_rad)*sin(g_rad)
    r6=sin(a_rad)*sin(b_rad)
    r7=-sin(b_rad)*cos(g_rad)
    r8=sin(b_rad)*sin(g_rad)
    r9=cos(b_rad)
    return np.array([[r1, r2, r3],
                     [r4, r5, r6],
                     [r7, r8, r9]])
r=eul2r(50,50,50)