from flask import Flask, request, render_template, redirect, url_for
import database

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = database.get_dictionary_of_users()
        if username in users and users[username][0] == password:
            print(1)
            return render_template('../../login/login.html', error=True)
        else:
            return render_template('/login/login.html', error=True)
    else:
        return render_template('teamplates/login/login.html', error=False)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        database.add_user(username, password)
    return render_template('/login/login.html', error=True)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
