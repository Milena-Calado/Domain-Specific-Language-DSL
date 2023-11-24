import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Softex2023",
    database="farmacia"
)

cursor = conexao.cursor()

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

conexao.commit()

cursor.close()
conexao.close()

