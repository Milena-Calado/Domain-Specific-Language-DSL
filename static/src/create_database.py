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
            id INT PRIMARY KEY,
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

if __name__ == "__main__":
    create_database()