from test_robot import TestRobot 

obj = TestRobot()

tickets = None
ticket = None
medicine = None
medicines = None
variable = None
pose = None
quantity = None


obj.connect('192.168.2.10')
obj.move_joints([10.291,42.895,106.288,267.739,332.335,92.869])
obj.move_joints([8.789, 340.573, 144.698, 269.934, 71.139, 90.942])
obj.retrieve_tickets()
while not len(tickets) == 0:
  for ticket in tickets:
    obj.retrieve_medicines(medicine, medicines)for medicine in medicines:
      obj.retrieve_pose(medicine, pose)
      obj.retrieve_quantity(medicine, quantity)
      for count in range(int(quantity)):
        obj.move_cartesiann()
    obj.move_joints([10.291,42.895,106.288,267.739,332.335,92.869])
    obj.move_joints([8.789, 340.573, 144.698, 269.934, 71.139, 90.942])
    obj.move_joints([10.291,42.895,106.288,267.739,332.335,92.869])
    obj.alerta_operacao_terminou()
  obj.retrieve_tickets()
obj.disconnect()