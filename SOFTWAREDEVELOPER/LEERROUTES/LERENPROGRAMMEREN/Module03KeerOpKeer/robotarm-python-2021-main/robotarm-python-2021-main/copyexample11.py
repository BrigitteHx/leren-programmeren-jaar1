from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:

while True: 
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveRight()
        True
    elif color == "":
        robotArm.wait()
    else:
        robotArm.drop()
        robotArm.moveRight()
        True

    # Na jouw code wachten tot het sluiten van de window:

