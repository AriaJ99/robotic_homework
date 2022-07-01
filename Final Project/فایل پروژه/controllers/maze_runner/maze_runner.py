from controller import Robot

# Get reference to the robot.
robot = Robot()

# Get simulation step length.
timeStep = int(robot.getBasicTimeStep())

# Constants of the e-puck motors and distance sensors.
maxMotorVelocity = 4.2
num_left_dist_sensors = 4
num_right_dist_sensors = 4
right_threshold = [75, 75, 75, 75]
left_threshold = [100, 100, 100, 100]
front_threshold = [100,100]

# Get left and right wheel motors.
leftMotor = robot.getDevice("left wheel motor")
rightMotor = robot.getDevice("right wheel motor")

# Get frontal distance sensors.
dist_right_sensors = [robot.getDevice('ps' + str(x)) for x in range(num_left_dist_sensors)]  # distance sensors
list(map((lambda s: s.enable(timeStep)), dist_right_sensors))  # Enable all distance sensors

dist_left_sensors = [robot.getDevice('ps' + str(x)) for x in range(num_right_dist_sensors,8)]  # distance sensors
list(map((lambda t: t.enable(timeStep)), dist_left_sensors))  # Enable all distance sensors

dist_front_sensors=[robot.getDevice('ps0'), robot.getDevice('ps7')]
list(map((lambda t: t.enable(timeStep)), dist_right_sensors))  # Enable all distance sensors

# Disable motor PID control mode.
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

# Set ideal motor velocity.
initialVelocity = 0.7 * maxMotorVelocity

# Set the initial velocity of the left and right wheel motors.
leftMotor.setVelocity(initialVelocity)
rightMotor.setVelocity(initialVelocity)

while robot.step(timeStep) != -1:
    
    left_dist_sensor_values = [g.getValue() for g in dist_left_sensors]
    right_dist_sensor_values = [h.getValue() for h in dist_right_sensors]
    front_dist_sensor_values= [f.getValue() for f in dist_front_sensors]
    left_obstacle = [(x > y) for x, y in zip(left_dist_sensor_values, left_threshold)]
    right_obstacle = [(m > n) for m, n in zip(right_dist_sensor_values, right_threshold)]
    front_obstacle = [(m > n) for m, n in zip(front_dist_sensor_values, front_threshold)]
 
    #lefMotor.setPosition(10)
    #rightMotor.setPostition(10)
    #if True in left_obstacle:
    #    leftMotor.setVelocity(initialVelocity-(0.5*initialVelocity))
    #    rightMotor.setVelocity(initialVelocity+(0.5*initialVelocity))
    print(right_obstacle)
    print(front_obstacle)
    
    leftMotor.setVelocity(initialVelocity)
    rightMotor.setVelocity(initialVelocity)
    if right_obstacle==[False,True,True,False]:
        if front_obstacle[1]==True:
            pass
        if front_obstacle[1]==False:
            pass
    if right_obstacle==[True,True,True,True]:
        if front_obstacle[1]==True:
            leftMotor.setVelocity(-initialVelocity)
            rightMotor.setVelocity(initialVelocity) 
        if front_obstacle[1]==False:
            pass
    if right_obstacle==[True, True, True, False]:
        leftMotor.setVelocity(-initialVelocity)
        rightMotor.setVelocity(initialVelocity)      
        if front_obstacle[1]==True:
            pass
        if front_obstacle[1]==False:
            pass
    if right_obstacle==[True,True,False,False]:
        leftMotor.setVelocity(-initialVelocity)
        rightMotor.setVelocity(initialVelocity)      

        if front_obstacle[1]==True:
            pass
        if front_obstacle[1]==False:
            pass
    if right_obstacle==[True,False,False,False]:
        leftMotor.setVelocity(initialVelocity-(0.5*initialVelocity))
        rightMotor.setVelocity(initialVelocity+(0.5*initialVelocity))   
        if front_obstacle[1]==True:
            pass
        if front_obstacle[1]==False:
            pass 
    if right_obstacle==[False,False,True,True]:
        leftMotor.setVelocity(initialVelocity+(0.5*initialVelocity))
        rightMotor.setVelocity(initialVelocity-(0.5*initialVelocity))   
        if front_obstacle[1]==True:
            pass
        if front_obstacle[1]==False:
            pass 
    if right_obstacle==[False,False,False,True]:
        if front_obstacle[1]==True:
            pass
        if front_obstacle[1]==False:
            pass 
    if right_obstacle==[False,False,False,False]:     
    
        if front_obstacle[1]==True:
            leftMotor.setVelocity(0)
            rightMotor.setVelocity(initialVelocity) 
        if front_obstacle[1]==False:
            leftMotor.setVelocity(initialVelocity+(0.5*initialVelocity))
            rightMotor.setVelocity(initialVelocity) 
    if right_obstacle==[False,False,True,False]:
        if front_obstacle[1]==True:
            pass
        if front_obstacle[1]==False:
            pass                        
    #if False in right_obstacle[0:2]:
     #   print('1')
      #  leftMotor.setVelocity(initialVelocity+(0.5*initialVelocity))
      #  rightMotor.setVelocity(initialVelocity-(0.5*initialVelocity))      
    
    #if front_obstacle[0]==True and front_obstacle[1]==True:
     #   print('true')
      #  leftMotor.setVelocity(initialVelocity-(0.5*initialVelocity))
       # rightMotor.setVelocity(initialVelocity+(0.5*initialVelocity))
    #if right_obstacle==[True,True,False,False] and front_obstacle==[True,False]:
     #   leftMotor.setVelocity(initialVelocity-(0.5*initialVelocity))
      #  rightMotor.setVelocity(initialVelocity+(0.5*initialVelocity))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        