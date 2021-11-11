from flask import Flask, render_template, url_for, request, session, redirect

import os
'''
template_dir = os.path.abspath('../../frontend/templates')
static_dir = os.path.abspath('../front_end/static')
'''
app = Flask(__name__, template_folder='../front_end/templates', static_folder='../front_end/static')

app.secret_key='secretkeyonlyIKnow'

class User:
    def __init__(self,id,username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}'

users = []
users.append(User(id=1, username='kaio', password = '1234'))

print(users)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method =='POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('register_page'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    return render_template('cadastro.html')

@app.route('/forgot_password')
def password_page():
    return render_template('fpassword.html')



if __name__ == "__main__":
    app.run(debug=True)