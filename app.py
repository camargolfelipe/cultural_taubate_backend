from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__, template_folder='../front_end/templates', static_folder='../front_end/static')

app.secret_key='secretkeyonlyIKnow'


class User:
    def __init__(self,id,username, password):
        self.id = id
        self.username = username
        self.password = password



user1 = User('kaio@gmail.com', 'Kaio', '1234')
user2 = User('gilberto@gmail.com', 'Gilberto Gil', 'maoi')

userList = {user1.id: user1,
            user2.id: user2}



@app.route('/')
def index():
    return render_template('login.html')

@app.route('/registrar')
def registrar():
    return render_template('cadastro.html')

@app.route('/cria_cadastro', methods=['POST'])
def cria_cadastro():
    
    id = request.form['useremail']
    username = request.form['username']
    password = request.form['password']

    user = User(id, username, password)
    

    return redirect('/')

@app.route('/autenticar', methods=['POST'])
def autenticar():

    if request.form['username'] in userList:
        usuario = userList[request.form['username']]
        if usuario.password == request.form['password']:
            session['usuario_logado'] = request.form['username']
            flash(usuario.username + ' logou com sucesso')
            return redirect('/perfil')

        else:
            flash('Login ou senha invalidos')
            return redirect('/')
    else:
        flash('Login ou senha invalidos')
        return redirect('/')
@app.route('/perfil')
def perfil():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/')
    else:
        return render_template('perfil.html', lista = userList)

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash("Nenhum usuario Logado")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)