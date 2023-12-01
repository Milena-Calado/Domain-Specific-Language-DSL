from robot import Robot 

obj = Robot()

obj.connect('192.168.2.10')
obj.move_joints([0, 0, 0, 0, 0, 0])