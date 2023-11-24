import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_code', methods=['POST'])
def run_code():
    try:
         # Receba o código gerado do corpo da solicitação
        data = request.get_json()
        generated_code = data.get('code')

      # Salve o código em um arquivo (opcional)
        with open('generated_code.py', 'w') as file:
            file.write('''from robot import Robot\n
obj = Robot()\n\n''')

            file.write(format(generated_code.rstrip('\n')))


            
        # Execute o código
        ret = subprocess.run(['python', 'generated_code.py'], check=True, capture_output=True)

      
    except Exception as e:
        # Trate exceções
        result = f"Erro ao executar o código: {e}"

    # Pode retornar resultados para o frontend se necessário
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
