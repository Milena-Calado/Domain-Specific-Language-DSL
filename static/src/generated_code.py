from test_robot import TestRobot 

obj = TestRobot()

tickets = None
ticket = None
medicines = None
medicine = None
pose = None
quantity = None


obj.execute_python_script('static\\src\\create_database.py')
obj.connect('192.168.2.10')
obj.move_joints([10.291,42.895,106.288,267.739,332.335,92.869])
obj.move_joints([8.789, 340.573, 144.698, 269.934, 71.139, 90.942])
obj.read_tickets('static\\src\\create_database.py', tickets)
while not len(tickets) == 0:
  for ticket in tickets:
    obj.read_medicines(tickets, medicines)
    for medicine in medicines:
      obj.read_pose(medicine, pose)
      obj.read_quantity(medicine, quantity)
      for count in range(int(quantity)):
        obj.open_tool(0.60)
        obj.move_cartesiann()
        obj.close_tool()
        obj.move_joints([10.291,42.895,106.288,267.739,332.335,92.869])
        obj.move_joints([8.789, 340.573, 144.698, 269.934, 71.139, 90.942])
        obj.open_tool(0.60)
        obj.move_joints([10.291,42.895,106.288,267.739,332.335,92.869])
    obj.alerta_operacao_terminou()
  obj.read_tickets('static\\src\\create_database.py', tickets)
obj.disconnect()