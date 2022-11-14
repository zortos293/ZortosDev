from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
for x in range(7):
    robotArm.moveRight()
    robotArm.grab()
    for z in range(8):
        robotArm.moveRight()
    robotArm.drop()    
    for z in range(9):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()