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
    nomes = ["Maria", "João", "Ana", "Pedro", "Luísa"]

    sobrenomes = ["Silva", "Santos", "Oliveira", "Souza"]

    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)

    nome_completo = f"{nome} {sobrenome}"
    return nome_completo

def populate_database():
    # Conectar ao MySQL
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Softex2023",
        database="farmacia"
    )

    cursor = conexao.cursor()

    # População da tabela 'setor'
    setores = [
        "NORTE 1",
        "NORTE 2",
        "SUL 1",
        "SUL 2"
    ]

    for setor_nome in setores:
        cursor.execute("INSERT INTO setor (nome) VALUES (%s)", (setor_nome,))
        conexao.commit()

    # População da tabela 'tickets'
    for _ in range(15):
        prontuario = random.randint(10000, 99999)
        paciente = gerar_nome_aleatorio()
        localizacao = gerar_localizacao()        
        medicamentos_quantidades = gerar_medicamentos_unicos()

        setor_id = random.randint(1, len(setores))

        consulta_nome_setor = "SELECT nome FROM setor WHERE id = %s"
        cursor.execute(consulta_nome_setor, (setor_id,))
        nome_setor = cursor.fetchone()[0]

        inserir_tickets = """
            INSERT INTO tickets 
            (prontuario, paciente, localizacao, setor, setor_nome, medicamento1, qtd_medicamento1,
             medicamento2, qtd_medicamento2, medicamento3, qtd_medicamento3)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        # Ajuste aqui: descompacte as tuplas para obter os valores individuais
        dados_tickets = (prontuario, paciente, localizacao, setor_id, nome_setor) + tuple(
            item for sublist in medicamentos_quantidades for item in sublist
        )
        cursor.execute(inserir_tickets, dados_tickets)
        conexao.commit()

    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()

    print("Tabelas populadas com sucesso.")

if __name__ == "__main__":
    populate_database()
