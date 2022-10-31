from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
for z in range(10):
    robotArm.moveRight()
for x in range(9):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()