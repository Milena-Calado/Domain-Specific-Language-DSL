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
        with open('static/src/generated_code.py', 'w') as file:
            #comente essa linha e descomente a debaixo para usar o robô de teste 
            # file.write('''from robot import Robot \n\nobj = Robot()\n\n''') 
            file.write('''from test_robot import TestRobot \n\nobj = TestRobot()\n\n''')

            file.write(format(generated_code.rstrip('\n')))       
            
        # Execute o código
        ret = subprocess.run(['python', 'static\src\generated_code.py'], shell=False)

         # Verifique se a execução foi bem-sucedida
        if ret.returncode == 0:
            result = "Código executado com sucesso."
        else:
            result = "Erro ao executar o código."
      
      
    except Exception as e:
        # Trate exceções
        result = f"Erro ao executar o código: {e}"

     # Pode retornar resultados para o frontend se necessário
    return jsonify(result)

if __name__ == '__main__':
    # Inicie o servidor Flask
    app.run(debug=False)