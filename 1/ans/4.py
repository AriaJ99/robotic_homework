import numpy as np
from math import radians, acos, sin, pi, degrees
def r2angvec(r):
    #function gets 3*3 matrix as input and returns corresponding rotation degree and
    #vector rotation was done about
    #return form : [theta, v]
    theta=acos((r[0][0]+r[1][1]+r[2][2]-1)/2)
    v=1/(2*sin(theta))*np.array([r[2][1]-r[1][2], r[0][2]-r[2][0], r[1][0]-r[0][1]])
    theta = degrees(theta)
    return [theta, v]
example=np.array([[1, 0.00000, 0.00000],
                  [0.00000, 0.64278761, -0.76604444],
                  [0.00000, 0.76604444, 0.64278761]])
[theta, v]=r2angvec(example)
print(theta,v)