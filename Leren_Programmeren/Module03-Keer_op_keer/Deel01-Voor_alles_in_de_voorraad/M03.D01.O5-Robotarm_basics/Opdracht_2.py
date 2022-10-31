from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:

robotArm.grab()
for x in range(9):
    robotArm.moveRight()
robotArm.drop()
for x in range(2):
    robotArm.moveLeft()
robotArm.grab()
for x in range(2):
    robotArm.moveRight()
robotArm.drop()
for x in range(5):
    robotArm.moveLeft()
robotArm.grab()
for x in range(5):
    robotArm.moveRight()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()