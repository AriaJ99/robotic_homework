from AIUT_RoboticsToolbox.Toolbox import *
import numpy as np
import scipy
import mpl_toolkits
import matplotlib
# import matplot3d
links=np.array([[0.00,0.00,0.00,0.00,0.00],
               [0.00,5.00,0.00,0.00,1.00],
               [np.pi/2,0.00,0,00,0.00,1.00]])
robot=SerialLink('figure 3_39',links)
robot.plot()
test1=robot.fkin([0.00,6.00,0.00])#only d2 moved
print(test1)
test2=robot.fkin([np.pi/2,0.00,0.00])#only theta one rotated
print(test2)
test3=robot.fkin([0.00,0.00,6.00])#only d3 moved
print(test3)
test4=robot.fkin([np.pi/2,6.00,8.00])#all joints moved
print(test4)