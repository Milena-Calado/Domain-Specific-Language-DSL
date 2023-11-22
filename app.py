from flask import Flask, render_template, request

app = Flask(__name__)


# Funções de exemplo para cada bloco Blockly
def connect():
    robot.connect()

def disconnect():
    robot.disconnect()

def move_to_home():
    robot.move_to_home()

def move_joints():
    robot.move_joints()

def move_cartesiann():
    robot.move_cartesiann()

def open_tool():
    robot.open_tool()

def close_tool():
    robot.close_tool()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    # Receba o código gerado do Blockly
    generated_code = request.form['code']

    # Salve o código em um arquivo (opcional)
    with open('generated_code.py', 'w') as file:
        file.write(generated_code)

    try:
        # Execute o código
        exec(generated_code)
        result = "Código executado com sucesso!"
    except Exception as e:
        # Trate exceções
        result = f"Erro ao executar o código: {e}"

    # Pode retornar resultados para o frontend se necessário
    return result

if __name__ == '__main__':
    app.run(debug=True)
