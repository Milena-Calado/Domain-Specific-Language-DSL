from robot import Robot

obj = Robot()

obj.connect('192.168.2.10')
if True:
  obj.move_to_home()
for count in range(2):
  obj.move_cartesiann([0, 0, 0, 0, 0, 0])
  obj.close_tool()
  obj.move_cartesiann([0, 0, 0, 0, 0, 0])
  obj.move_cartesiann([0, 0, 0, 0, 0, 0])
  obj.open_tool(0.60)
obj.move_cartesiann([0, 0, 0, 0, 0, 0])
obj.close_tool()
obj.move_cartesiann([0, 0, 0, 0, 0, 0])
obj.move_cartesiann([0, 0, 0, 0, 0, 0])
obj.open_tool(0.60)
obj.move_to_home()
obj.disconnect()