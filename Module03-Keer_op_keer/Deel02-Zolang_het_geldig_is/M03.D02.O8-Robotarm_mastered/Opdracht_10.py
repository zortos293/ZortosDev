from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

for x in range(5):
    for z in range(x):
        robotArm.moveRight()
    robotArm.grab()
    for z in range(9 -x -x):
        robotArm.moveRight()
    robotArm.drop()
    for d in range(9 + x):
        robotArm.moveLeft()    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()