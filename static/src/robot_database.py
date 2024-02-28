import mysql.connector

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
