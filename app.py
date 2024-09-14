from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
# // Importa framework Flask para realizar a captação dos dados do form
app = Flask(__name__) # Cria a instância do Flask

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'cadastro',
)
# // Inicializa conexão ao banco de dados //

cursor = conexao.cursor()
# // Cursor recebe conexão e a executa. //

@app.route('/')
def formulario():
    return render_template('index.html')
# // Rota para pagina inicial

@app.route('/armazenar_dados', methods=['POST'])
def armazenar_dados():
    # Pega os dados do formulário e armazena em variaveis
    nomeCompleto = request.form['nomeCompleto']
    telefoneContato = request.form['telefoneContato']
    dataNascimento = request.form['dataNascimento']
    rendaMensal = float(request.form['rendaMensal'])
    numeroFilhos = int(request.form['numeroFilhos'])
    email = request.form['email']
    pais = request.form['pais']
    estado = request.form['estado']
    cidade = request.form['cidade']
    bairro = request.form['bairro']
    nomeRua = request.form['nomeRua']
    numeroResidencial = request.form['numeroResidencial']
    
    query = """
    INSERT INTO clientes (nomeCompleto, telefoneContato, dataNascimento, rendaMensal, numeroFilhos, email, pais, estado, cidade, bairro, nomeRua, numeroResidencial)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    # Inserir no MySQL
    valores = (nomeCompleto, telefoneContato, dataNascimento, rendaMensal, numeroFilhos, email, pais, estado, cidade, bairro, nomeRua, numeroResidencial)
    cursor = conexao.cursor()
    cursor.execute(query, valores)
    conexao.commit()  # Confirmando o envio

    # Fechando a conexão com o banco de dados
    cursor.close()

    # Redirecionando para a página inicial
    return redirect(url_for('formulario'))


if __name__ == '__main__':
    app.run(debug=True)

    
    
    

