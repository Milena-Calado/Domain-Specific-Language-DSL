from test_robot import TestRobot 

obj = TestRobot()

obj.create_database()
obj.create_ticket('Milena', 'Setor A')
obj.create_ticket('Joao ', 'Setor B')
obj.create_medicamento('Colistemato', '2')
obj.create_medicamento('Fentanila ', '1')
obj.adicionar_medicamento_ao_ticket(1, 1)