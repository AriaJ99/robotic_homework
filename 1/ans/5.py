import numpy as np
from math import radians, acos, sin, pi, degrees
from scipy.linalg import expm, logm
def angvec2r_2(theta, v):
    #second version of angvec2r which uses R=exp(V*theta) equation
    theta=radians(theta)
    print(theta)
    return expm(theta*np.array([[0, -v[2], v[1]],
                                 [v[2], 0, -v[0]],
                                 [-v[1], v[0], 0]]))

def r2angvec_2(r):
    #second version of r2angvec which uses R=exp(V*theta) equation
    #input is a 3*3 numpy rotation matrix
    theta = acos((r[0][0] + r[1][1] + r[2][2] - 1) / 2)
    l=logm(r)

    #l=V*theta


    l/=theta
    theta = degrees(theta)
    #l=V

    v=np.array([l[2][1], l[0][2], l[1][0]])
    return [theta,v]
example=np.array([[1, 0.00000, 0.00000],
                  [0.00000, 0.64278761, -0.76604444],
                  [0.00000, 0.76604444, 0.64278761]])

print(angvec2r_2(50,np.array([1,0,0])))
[theta,v]=r2angvec_2(example)
print(theta, v)