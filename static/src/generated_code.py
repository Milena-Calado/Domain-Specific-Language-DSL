from test_robot import TestRobot 

obj = TestRobot()

obj.connect('192.168.2.10')
obj.execute_python_script('static/src/create_database.py')