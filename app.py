import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_code', methods=['GET'])
def run_code():
    try:
         # Receba o código gerado do Blockly
        generated_code = str(request.data, 'utf-8')

      # Salve o código em um arquivo (opcional)
        with open('generated_code.py', 'w') as file:
            file.write(generated_code)
   
        # Execute o código
        ret = subprocess.run(['python', 'generated_code.py'], check=True, capture_output=True)
        print(ret)
        result = {
            'stdout': ret.stdout.decode('utf-8'),
            'stderr': ret.stderr.decode('utf-8'),
            'returncode': ret.returncode

        }

    except Exception as e:
        # Trate exceções
        result = f"Erro ao executar o código: {e}"

    # Pode retornar resultados para o frontend se necessário
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
