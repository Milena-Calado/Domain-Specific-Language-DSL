from test_robot import TestRobot 

obj = TestRobot()

ticket = None
tickets = None
medicine = None
medicines = None
pose = None
poses = None
quantity = None


obj.connect('192.168.2.10')
obj.move_joints([10.291,42.895,106.288,267.739,332.335,92.869])
obj.move_joints([8.789, 340.573, 144.698, 269.934, 71.139, 90.942])
obj.execute_python_script('Path file')
obj.retrieve_tickets()
while not len(tickets) == 0:
  for ticket in tickets:
    obj.retrieve_medicines()
    for medicine in medicines:
      obj.retrieve_pose()
      for pose in poses:
        obj.retrieve_quantity()
        for count in range(int(quantity)):
          obj.move_cartesiann([0, 0, 0, 0, 0, 0])
          obj.move_cartesiann([0, 0, 0, 0, 0, 0])
obj.move_joints([10.291,42.895,106.288,267.739,332.335,92.869])
obj.move_joints([8.789, 340.573, 144.698, 269.934, 71.139, 90.942])
obj.wait_dispensed()
obj.disconnect()