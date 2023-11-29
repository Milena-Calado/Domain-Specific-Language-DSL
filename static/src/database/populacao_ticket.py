import mysql.connector
import random
import string

def gerar_localizacao():
    numeros = ''.join(random.choice(string.digits) for _ in range(4))
    letra = random.choice(string.ascii_uppercase)
    return f"{numeros}{letra}"

def gerar_medicamentos_unicos():
    medicamentos = [
        f"02 - colistimetato de sódio - {random.randint(1, 2)}",        
        f"05 - tigeciclina - {random.randint(1, 2)}",
        f"1220 - Fentanila - {random.randint(1, 2)}",
       
    ]
    medicamentos_unicos = random.sample(medicamentos, 3)
    return medicamentos_unicos

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

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Softex2023",
    database="farmacia"
)

cursor = conexao.cursor()

setores = list(range(1, 8))

for setor in setores:
    for _ in range(15):
        prontuario = random.randint(10000, 99999)
        paciente = gerar_nome_aleatorio()
        localizacao = gerar_localizacao()        
        medicamentos_unicos = gerar_medicamentos_unicos()

        consulta_nome_setor = "SELECT nome FROM setor WHERE id = %s"
        cursor.execute(consulta_nome_setor, (setor,))
        nome_setor = cursor.fetchone()[0]

        inserir_tickets = """
            INSERT INTO tickets (prontuario, paciente, localizacao, setor, setor_nome, emissor, medicamento1, medicamento2, medicamento3)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        dados_tickets = (prontuario, paciente, localizacao, setor, nome_setor, emissao) + tuple(medicamentos_unicos)
        cursor.execute(inserir_tickets, dados_tickets)

conexao.commit()

cursor.close()
conexao.close()