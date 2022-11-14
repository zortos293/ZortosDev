from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
for x in range(10):
    if x == 1 :
        robotArm.moveRight()
    elif x  == 3 :   
        robotArm.moveRight()
    elif x ==  6 :
        robotArm.moveRight() 
    elif x ==  10 :
        break    
    
    robotArm.grab()
    for z in range(5):
        robotArm.moveRight()
    robotArm.drop() 
    for l in range(5):
        robotArm.moveLeft()
        

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()