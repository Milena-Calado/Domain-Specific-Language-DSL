import mysql.connector
import random
import string

def gerar_localizacao():
    numeros = ''.join(random.choice(string.digits) for _ in range(4))
    letra = random.choice(string.ascii_uppercase)
    return f"{numeros}{letra}"

def gerar_medicamentos_unicos():
    medicamentos = [
        "Colistimetato de sódio",
        "Tigeciclina",
        "Fentanila",
    ]
    
    medicamentos_unicos = random.sample(medicamentos, 3)
    
    # Gere uma quantidade aleatória para cada medicamento
    quantidades_medicamentos = [random.randint(1, 2) for _ in range(3)]

    # Combine os medicamentos e suas quantidades em tuplas
    medicamentos_quantidades = list(zip(medicamentos_unicos, quantidades_medicamentos))

    return medicamentos_quantidades


def gerar_nome_aleatorio():
    nomes = ["Maria", "João", "Ana", "Pedro", "Luísa", "Felipe", "Beatriz", "Rafael", "Carolina", "Thiago",
    "Mariana", "Gustavo", "Camila", "Lucas", "Juliana", "Diego", "Larissa", "André", "Isabela", "Daniel",
    "Bianca", "Fernando", "Natália", "Ricardo", "Amanda", "Rodrigo", "Patrícia", "Eduardo", "Vanessa"]

    sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Costa", "Rodrigues", "Ferreira", "Almeida", "Carvalho",
    "Gomes", "Martins", "Lima", "Araújo", "Fernandes", "Ribeiro", "Sousa", "Rocha", "Barbosa", "Machado",
    "Gonçalves", "Vieira", "Tavares", "Correia", "Cardoso", "Lopes", "Nunes", "Cavalcanti", "Mendes"]

    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)

    nome_completo = f"{nome} {sobrenome}"
    return nome_completo

def create_and_populate_database():
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
            prontuario INT PRIMARY KEY,
            paciente VARCHAR(255) NOT NULL,
            localizacao VARCHAR(255) NOT NULL,
            setor INT,
            setor_nome VARCHAR(255),        
            medicamento1 VARCHAR(255),
            qtd_medicamento1 INT,  -- Nova coluna para quantidade de medicamento1
            medicamento2 VARCHAR(255),
            qtd_medicamento2 INT,  -- Nova coluna para quantidade de medicamento2
            medicamento3 VARCHAR(255),
            qtd_medicamento3 INT,  -- Nova coluna para quantidade de medicamento3
            status_processo BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (setor) REFERENCES setor(id)
        )
    """)

    # População da tabela 'setor'
    setores = [
        "9º NORTE",
        "11º NORTE",
        "URGENCIA E EMERGENCIA",
        "11º SUL",
        "9º SUL",
        "8º NORTE",
        "8º SUL"
    ]

    for setor_nome in setores:
        cursor.execute("INSERT INTO setor (nome) VALUES (%s)", (setor_nome,))

    # População da tabela 'tickets'
    setores = list(range(1, 8))

    for setor in setores:
        for _ in range(15):
            prontuario = random.randint(10000, 99999)
            paciente = gerar_nome_aleatorio()
            localizacao = gerar_localizacao()        
            medicamentos_quantidades = gerar_medicamentos_unicos()

            consulta_nome_setor = "SELECT nome FROM setor WHERE id = %s"
            cursor.execute(consulta_nome_setor, (setor,))
            nome_setor = cursor.fetchone()[0]

            inserir_tickets = """
                INSERT INTO tickets 
                (prontuario, paciente, localizacao, setor, setor_nome, medicamento1, qtd_medicamento1,
                 medicamento2, qtd_medicamento2, medicamento3, qtd_medicamento3)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            # Ajuste aqui: descompacte as tuplas para obter os valores individuais
            dados_tickets = (prontuario, paciente, localizacao, setor, nome_setor) + tuple(
                item for sublist in medicamentos_quantidades for item in sublist
            )
            cursor.execute(inserir_tickets, dados_tickets)

    # Commit para salvar as alterações
    conexao.commit()

    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()

    print("Banco de dados e tabelas criados e populados com sucesso.")

if __name__ == "__main__":
    create_and_populate_database()
