from flask import Flask, render_template, request, redirect, session, flash, url_for
from connection import collection

app = Flask(__name__, template_folder='../front_end/templates', static_folder='../front_end/static')

app.secret_key='secretkeyonlyIKnow'


class User:
    def __init__(self,id,username, password):
        self.id = id
        self.username = username
        self.password = password


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar')
def registrar():
    return render_template('cadastro.html')


@app.route('/cria_cadastro', methods=['POST','GET'])
def cria_cadastro():
    
    id = request.form['useremail']
    username = request.form['username']
    password = request.form['password']

    resultado = collection.find_one({"username":username})
    #dbAcc = resultado['username']


    cadastro = {"ID": f"{id}", "username": f"{username}","password": f"{password}"}
    collection.insert_one(cadastro)
    return redirect(url_for("login"))

# LOGIN AREA
@app.route("/login")
def login():
    return render_template('login.html')
   

@app.route('/autenticar', methods=['POST',])
def autenticar():

    id = request.form['id']
    password = request.form['password']
    resultado = collection.find({"ID":f"{id}"})  
    
    for i in resultado:
        dbPass = i['password']
        dbAcc = i['ID']

        if dbAcc == id and dbPass == password:
            session['usuario_logado'] = i['username']
            
            return redirect(url_for('perfil'))
        else:
            flash('Login ou senha invalidos')
            return redirect('/')
    

@app.route('/perfil/<nome>')
def perfil(nome):    
    return render_template('perfil.html')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash("Nenhum usuario Logado")
    return redirect('/')

@app.route('/mudar_senha')
def muda_senha():
    return render_template('fpassword.html')

@app.route("/eventos")
def eventos():
    pass

@app.route("/contato")
def contato():
    pass

if __name__ == "__main__":
    app.run(debug=True)