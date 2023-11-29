import mysql.connector

# Função para mover o robô com base nos medicamentos e quantidades
def mover_robo(medicamento, quantidade):
    if medicamento == 'Colistimetato de sódio':
        code = 'obj.move_joints([295.18951416015625, 309.2252197265625, 116.1842041015625, 295.02618408203125, 80.2393798828125, 85.50155639648438])\nobj.move_cartesiann([0.1557641625404358, -0.44633567333221436, 0.12219314277172089, 87.29951477050781, -0.5001964569091797, 15.019988059997559])\nobj.move_cartesiann([0.20072071254253387, -0.5997055172920227, 0.12531529366970062, 88.035400390625, -0.2923136055469513, 14.742742538452148])\nobj.close_tool()\nobj.move_joints([308.3565368652344, 293.7962341308594, 114.3787841796875, 293.5994873046875, 93.23373413085938, 90.71200561523438])\nobj.move_joints([15.547500610351562, 293.7962341308594, 114.3787841796875, 293.5994873046875, 93.23373413085938, 90.71200561523438])\nobj.move_joints([5.11016845703125, 338.84356689453125, 99.62835693359375, 266.817138671875, 325.823486328125, 12.781982421875])\nobj.move_joints([5.1771087646484375, 315.9814453125, 96.06057739257812, 262.8784484863281, 345.0887756347656, 17.115264892578125])\nobj.open_tool(0.60)\n'
        for i in range(quantidade):
            # Lógica de movimento do robô para o medicamento Colistimetato de sódio
            print(f'Movimento do robô para {medicamento} - Iteração {i+1}')
    elif medicamento == 'Tigeciclina':
        code = 'obj.move_joints([295.18951416015625, 309.2252197265625, 116.1842041015625, 295.02618408203125, 80.2393798828125, 85.50155639648438])\nobj.move_cartesiann([0.1557641625404358, -0.44633567333221436, 0.12219314277172089, 87.29951477050781, -0.5001964569091797, 15.019988059997559])\nobj.move_cartesiann([0.20072071254253387, -0.5997055172920227, 0.12531529366970062, 88.035400390625, -0.2923136055469513, 14.742742538452148])\nobj.close_tool()\nobj.move_joints([308.3565368652344, 293.7962341308594, 114.3787841796875, 293.5994873046875, 93.23373413085938, 90.71200561523438])\nobj.move_joints([15.547500610351562, 293.7962341308594, 114.3787841796875, 293.5994873046875, 93.23373413085938, 90.71200561523438])\nobj.move_joints([5.11016845703125, 338.84356689453125, 99.62835693359375, 266.817138671875, 325.823486328125, 12.781982421875])\nobj.move_joints([5.1771087646484375, 315.9814453125, 96.06057739257812, 262.8784484863281, 345.0887756347656, 17.115264892578125])\nobj.open_tool(0.60)\n'
        for i in range(quantidade):
            # Lógica de movimento do robô para o medicamento Tigeciclina
            print(f'Movimento do robô para {medicamento} - Iteração {i+1}')
    elif medicamento == 'Fentanila':
        code = 'obj.move_joints([295.18951416015625, 309.2252197265625, 116.1842041015625, 295.02618408203125, 80.2393798828125, 85.50155639648438])\nobj.move_cartesiann([-0.011559383943676949, -0.42786967754364014, 0.2772851288318634, 88.28321075439453, -0.8314085602760315, 0.5609025359153748])\nobj.move_cartesiann([-0.01142274122685194, -0.6069214344024658, 0.28211238980293274, 87.37435913085938, -0.9280807971954346, 0.5559726357460022])\nobj.close_tool()\nobj.move_joints([285.50921630859375, 338.14031982421875, 135.8863525390625, 285.9048156738281, 70.42501831054688, 84.9200439453125])\nobj.move_joints([15.547500610351562, 338.14031982421875, 135.8863525390625, 285.9048156738281, 70.42501831054688, 84.9200439453125])\nobj.move_joints([5.11016845703125, 338.84356689453125, 99.62835693359375, 266.817138671875, 325.823486328125, 12.781982421875])\nobj.move_joints([5.1771087646484375, 315.9814453125, 96.06057739257812, 262.8784484863281, 345.0887756347656, 17.115264892578125])\nobj.open_tool(0.60)\n'
        for i in range(quantidade):
            # Lógica de movimento do robô para o medicamento Fentanila
            print(f'Movimento do robô para {medicamento} - Iteração {i+1}')
    else:
        print(f'Medicamento não reconhecido: {medicamento}')


# Conectar ao MySQL usando o banco de dados 'farmacia'
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Softex2023",
    database="farmacia"
)

cursor = conexao.cursor(dictionary=True)

# Consultar os tickets
cursor.execute("SELECT * FROM tickets WHERE status_processo = FALSE")
tickets = cursor.fetchall()

# Iterar sobre os tickets
for ticket in tickets:
    prontuario = ticket['prontuario']
    paciente = ticket['paciente']
    localizacao = ticket['localizacao']
    setor_nome = ticket['setor_nome']

    # Adapte a lógica para os medicamentos específicos que você possui
    medicamento = ticket['medicamento1']
    quantidade = ticket['quantidade_medicamento1']

    if medicamento and quantidade:
        # Mover o robô com base no medicamento e quantidade
        mover_robo(medicamento, quantidade)
        
        # Marcar o ticket como processado
        cursor.execute("UPDATE tickets SET status_processo = TRUE WHERE prontuario = %s", (prontuario,))
        conexao.commit()

# Fechar o cursor e a conexão
cursor.close()
conexao.close()
