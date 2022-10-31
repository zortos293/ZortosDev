from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
moved_right = 1
movee = 0
for z in range(7):
    robotArm.grab()
    if robotArm.scan() != '':
        movee = movee +1
        for o in range(movee):
            robotArm.moveRight()
            

        robotArm.drop()
        for z in range(moved_right):
            robotArm.moveLeft()
        moved_right = moved_right+1
    else:
        break





