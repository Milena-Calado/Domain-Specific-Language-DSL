import mysql.connector

def create_database():
    # Conectar ao MySQL
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Softex2023"
    )
    cursor = conexao.cursor()

    # Remover o banco de dados caso ele exista
    cursor.execute("DROP DATABASE IF EXISTS farmacia")

    # Criar o banco de dados
    cursor.execute("CREATE DATABASE IF NOT EXISTS farmacia")

    # Selecionar o banco de dados
    cursor.execute("USE farmacia")

    # Criar a tabela 'setor' se não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS setor (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL
        )
    """)
    
    # Criar a tabela 'tickets' se não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INT AUTO_INCREMENT PRIMARY KEY,
            paciente VARCHAR(255) NOT NULL,
            localizacao VARCHAR(255) NOT NULL,
            setor INT,
            setor_nome VARCHAR(255),
            status_processo BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (setor) REFERENCES setor(id)
        )
    """)

    # Criar a tabela 'medicamentos' se não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicamentos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            quantidade INT,
            pose VARCHAR(50)
        )
    """)

    # Criar a tabela 'medicamentos_tickets' para armazenar os medicamentos associados aos tickets
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicamentos_tickets (
            id_ticket INT,
            id_medicamento INT,
            qtd_medicamento INT,
            pose_medicamento VARCHAR(50),
            FOREIGN KEY (id_ticket) REFERENCES tickets(id),
            FOREIGN KEY (id_medicamento) REFERENCES medicamentos(id)
        )
    """)

    # Commit para salvar as alterações
    conexao.commit()

    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()

    print("Banco de dados e tabelas criados com sucesso.")

def create_ticket(paciente, localizacao, setor_id, setor_nome):
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Softex2023",
            database="farmacia"
        )

        cursor = conexao.cursor()

        # Inserir os dados do ticket na tabela 'tickets'
        cursor.execute("""
            INSERT INTO tickets (paciente, localizacao, setor, setor_nome)
            VALUES (%s, %s, %s, %s)
        """, (paciente, localizacao, setor_id, setor_nome))

        # Commit para salvar as alterações
        conexao.commit()

        print("Ticket criado com sucesso.")

    except Exception as e:
        print(f"Erro ao criar ticket: {e}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

def create_medicamento(nome, quantidade, pose):
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Softex2023",
            database="farmacia"
        )

        cursor = conexao.cursor()

        # Inserir os dados do medicamento na tabela 'medicamentos'
        cursor.execute("""
            INSERT INTO medicamentos (nome, quantidade, pose)
            VALUES (%s, %s, %s)
        """, (nome, quantidade, pose))

        # Commit para salvar as alterações
        conexao.commit()

        print("Medicamento criado com sucesso.")

    except Exception as e:
        print(f"Erro ao criar medicamento: {e}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conexao.close()

if __name__ == "__main__":
    create_database()
