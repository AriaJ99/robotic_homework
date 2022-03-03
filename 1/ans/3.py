import numpy as np
from math import radians, cos, sin, pi
def angvec2r(theta, v):
    #function returns a matrix for rotating about v vector
    #v must be a numpy array and also unit vector
    rad=radians(theta)
    c=cos(rad)
    s=sin(rad)
    e=1-c
    x=v[0]
    y=v[1]
    z=v[2]
    return np.array([[x*x*e+c, x*y*e-z*s, x*z*e+y*s],
                     [x*y*e+z*s, y*y*e+c, y*z*e-x*s],
                     [x*z*e-y*s, y*z*e+x*s, z*z*e+c]])
r=angvec2r(50,np.array([1,0,0]))
print(r)