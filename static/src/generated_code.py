from test_robot import TestRobot 

obj = TestRobot()

obj.connect('192.168.2.10')
obj.move_joints([0, 0, 0, 0, 0, 0])
obj.alerta_operacao_terminou()