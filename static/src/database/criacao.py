import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Softex2023"
)

cursor = conexao.cursor()

# remover o banco de dados caso ele exista
cursor.execute("DROP DATABASE IF EXISTS farmacia")

cursor.execute("CREATE DATABASE IF NOT EXISTS farmacia")

cursor.execute("USE farmacia")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS setor (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        prontuario INT PRIMARY KEY,
        paciente VARCHAR(255) NOT NULL,
        localizacao VARCHAR(255) NOT NULL,
        setor INT,
        setor_nome VARCHAR(255),
        emissor VARCHAR(255),
        medicamento1 VARCHAR(255),
        medicamento2 VARCHAR(255),
        medicamento3 VARCHAR(255),
        status_processo BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (setor) REFERENCES setor(id)
    )
""")

cursor.close()
conexao.close()

print("Banco de dados e tabelas criados com sucesso.")
