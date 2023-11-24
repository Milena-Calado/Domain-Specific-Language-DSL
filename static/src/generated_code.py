from robot import Robot

obj = Robot()

obj.connect('192.168.2.10')
if True:
  obj.move_to_home()
  obj.open_tool(0.7)
obj.move_cartesian([0, 0, 0, 0, 0, 0])
obj.close_tool()
obj.move_to_home()
obj.move_cartesian([0, 0, 0, 0, 0, 0])
obj.open_tool(0.7)
obj.move_to_home()
obj.disconnect()