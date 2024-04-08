import mysql.connector

def ler_tabela_tickets(cursor):
    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()
    print("Tabela 'tickets':")
    for ticket in tickets:
        print(ticket)

def ler_tabela_medicamentos(cursor):
    cursor.execute("SELECT * FROM medicamentos")
    medicamentos = cursor.fetchall()
    print("\nTabela 'medicamentos':")
    for medicamento in medicamentos:
        print(medicamento)

def ler_tabela_medicamentos_tickets(cursor):
    cursor.execute("SELECT * FROM medicamentos_tickets")
    medicamentos_tickets = cursor.fetchall()
    print("\nTabela 'medicamentos_tickets':")
    for mt in medicamentos_tickets:
        print(mt)

    # Conectar ao MySQL
    conexao = mysql.connector.connect(host="localhost", user="root", password="Softex2023", database="farmacia")

    cursor = conexao.cursor()

    # Chamar as funções para ler cada tabela
    ler_tabela_tickets(cursor)
    ler_tabela_medicamentos(cursor)
    ler_tabela_medicamentos_tickets(cursor)

    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()
