from flask import Flask, request, url_for, redirect, render_template, flash
from modelo.cliente import Cliente

# instanciando objetos para teste
clientes = [Cliente(1, "Pablo Granch", 100, '305.180.330-82', 'fisica'),
            Cliente(2, "Manu Rios", 200, '485.069.310-53', 'fisica'),
            Cliente(3, "Martina Cariddi", 300, '601.046.020-40', 'fisica'),
            Cliente(4, "Claudia Salas", 400, '448.659.850-42', 'fisica'),
            Cliente(5, "Jorge Lopez", 500, '047.296.140-38', 'fisica')]
id_atual = 6
codigo_atual = 600


def atualiza_clientes(cliente):
    global id_atual
    global codigo_atual
    id_atual += 1
    codigo_atual += 100
    clientes.append(cliente)


def apagar_clientes(cliente):
    clientes.remove(cliente)


# instanciando o app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'senha'


# botando Controller pra funcionar
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


# POST - Create do CRUD
@app.route('/login', methods=['GET', 'POST'])
def set_cliente():
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['cpf']:
            flash('Favor entrar todos os valores dos campos')
        else:
            cliente = Cliente(id_atual, request.form['nome'], codigo_atual, request.form['cpf'], 'fisica')
            atualiza_clientes(cliente)
            flash('Registro foi inserido com sucesso')
            return redirect(url_for('show_clientes'))
    return render_template('form.html')


# GET - Read do CRUD
@app.route('/cliente/<int:cliente_id>')
@app.route('/cliente', defaults={'cliente_id': None})
def get_cliente(cliente_id):
    if cliente_id:
        try:
            cliente = [c for c in clientes if cliente_id == c.get_id()][0]
            return render_template('cliente.html', cliente=cliente)
        except IndexError as e:
            return render_template('cliente.html', erro=e)
    else:
        return render_template('cliente.html')


# PUT - Update do CRUD
@app.route('/atualizar', methods=['GET', 'POST'])
def atualiza_cliente():
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['cpf'] or not request.form['id']:
            flash('Favor entrar todos os valores dos campos')
        else:
            try:
                cliente_id = int(request.form['id'])
                cliente = [c for c in clientes if cliente_id == c.get_id()][0]
                cliente.set_nome(request.form['nome'])
                cliente.set_cnpjcpf(request.form['cpf'])
                flash('Registro foi atualizado com sucesso')
                return redirect(url_for('show_clientes'))
            except IndexError as e:
                flash(f'Favor entre com um id válido.')
    return render_template('atualizar.html')


# DELETE - Delete do CRUD
@app.route('/deletar/<int:cliente_id>')
@app.route('/deletar', defaults={'cliente_id': None})
def apagar_cliente(cliente_id):
    if cliente_id:
        try:
            cliente = [c for c in clientes if cliente_id == c.get_id()][0]
            apagar_clientes(cliente)
            return render_template('deletar.html', cliente=cliente)
        except IndexError as e:
            return render_template('deletar.html', erro=e)
    else:
        return render_template('deletar.html')


# mostrar todos os clientes
@app.route('/clientes')
def show_clientes():
    return render_template('clientes.html', clientes=clientes)


# inicio do app
if __name__ == '__main__':
    app.run()
