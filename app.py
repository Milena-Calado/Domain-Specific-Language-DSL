import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_code', methods=['POST'])
def run_code():
    try:
        # Receba o código gerado do Blockly
        generated_code = request
        print(generated_code)

      # Salve o código em um arquivo (opcional)
        with open('generated_code.py', 'w') as file:
            file.write(generated_code)

   
        # Execute o código
        ret = subprocess.run(['python', 'generated_code.py'], shell=True)
        print(ret)
        result = "Código executado com sucesso!"

    except Exception as e:
        # Trate exceções
        result = f"Erro ao executar o código: {e}"

    # Pode retornar resultados para o frontend se necessário
    return result

if __name__ == '__main__':
    app.run(debug=True)
