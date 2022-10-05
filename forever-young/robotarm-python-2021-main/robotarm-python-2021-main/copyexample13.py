from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 3
teller = 1 
while teller > 0 or teller < 10:
    robotArm.grab()
    color = robotArm.scan()
    if color == "red" or "green" or "yellow" or "blue" or "white":
        for i in range (teller):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(teller):
            robotArm.moveLeft()
        teller = teller + 1
    if color == '': 
        break
robotArm.wait()