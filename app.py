from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/executar_codigo', methods=['POST'])
def executar_codigo():
    codigo_python = request.form['codigo_python']
    # Execute o código Python aqui
    # ...

    # Retorne o resultado para o Blockly
    resultado = "Resultado da execução do código"
    return resultado

if __name__ == '__main__':
    app.run(debug=True)
