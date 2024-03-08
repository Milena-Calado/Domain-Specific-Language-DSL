from test_robot import TestRobot 

obj = TestRobot()

obj.create_database()
obj.create_ticket('Milena', 'Setor A')
obj.create_medicamento('Colistemato de sodio', 2, 'dfdfsfdfsdfd')
obj.adicionar_medicamento_ao_ticket('Milena', 'Colistemato de sodio', 1)