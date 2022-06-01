"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot,Motor
import sys
import math
# create the Robot instance.
def initialize_bots(robot,robot_parts):
     robot_parts[0].setVelocity(0.7)
     robot_parts[1].setVelocity(0.2)
     robot_parts[2].setVelocity(0.7)
def test(robot,robot_parts):
    for bot in robot_parts:
      
        bot.setPosition(1)
        robot.step(50*timestep)
        
        bot.setPosition(-1)
        robot.step(200*timestep)
        bot.setPosition(0)
        robot.step(100*timestep)
def find_joint_parameters(x,y,z):
    if x==0:
        theta=-math.pi/2
            
    else:
        theta=math.atan(y/x)
    r=math.sqrt(y**2+x**2)
 
    return theta,r
def check_coordinate_validation(l,x,y,z):
    if(z!=0):
        print(z,'coordination is out of robot subspace')
        exit()
    if(x**2+y**2>l**2):
        print('coordination is out of workspace')
        exit()
    print('coordination is reachable for the bot')
def transform_bot(robot,robot_parts,theta,r,l):

     robot_parts[0].setPosition(theta)
     robot.step(100*timestep)
     robot_parts[1].setPosition(r-l/2)   
     #robot_parts[1].setPosition(r)
robot = Robot()
y,x,z=list(map(float,sys.argv[1].split()))
x*=-1
print(x,y,z)
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
robot_parts=[]
robot_parts_names=['axis_1_motor','axis_2_motor','axis_3_motor']
for name in robot_parts_names:
    robot_parts.append(robot.getDevice(name))
l=0.53

initialize_bots(robot,robot_parts)
test(robot,robot_parts)
#print(atan(float(1)/float(0)))
check_coordinate_validation(l,x,y,z)
theta,r=find_joint_parameters(x,y,z) 
print(theta,r)
transform_bot(robot,robot_parts,theta,r,l)
# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
