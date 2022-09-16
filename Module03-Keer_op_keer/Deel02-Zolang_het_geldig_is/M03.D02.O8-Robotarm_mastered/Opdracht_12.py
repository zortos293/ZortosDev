from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

moved_right = 1
for x in range (10):
    robotArm.grab()
    if robotArm.scan() == 'red':
        for p in range(10-moved_right):
            robotArm.moveRight()
        robotArm.drop()
        for z in range(10 -moved_right):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
        moved_right = moved_right +1        

    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()