import mysql.connector

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

        # Criar a tabela 'tickets' se não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INT AUTO_INCREMENT PRIMARY KEY,
        paciente VARCHAR(255) NOT NULL,                   
        setor_nome VARCHAR(255),
        status_processo BOOLEAN DEFAULT FALSE
    )
""")

# Criar a tabela 'medicamentos' se não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicamentos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,   
        quantidade INT NOT NULL,                 
        pose VARCHAR(50)
    )
""")

# Criar a tabela 'medicamentos_tickets' para armazenar os medicamentos associados aos tickets
cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicamentos_tickets (
        id_ticket INT,
        paciente VARCHAR(255),
        setor_nome VARCHAR(255),
        id_medicamento INT,
        nome VARCHAR(255),
        quantidade INT,
        pose VARCHAR(50),
        status_processo BOOLEAN DEFAULT FALSE,
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
