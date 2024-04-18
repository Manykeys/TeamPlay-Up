from flask import Flask, request, render_template, redirect, url_for
import database

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main_page.html', error=False)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = database.get_dictionary_of_users()
        print(users)
        if username in users and users[username][0] == password:
            print(2)
            return render_template('menu.html')
        else:
            error_message = 'Incorrect username or password. Please try again.'
            return render_template('login.html', error=True,
                                   error_message=error_message)
    else:
        return render_template('login.html', error=False)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        dict = database.get_dictionary_of_users()
        if username in dict.keys():
            error_message = 'Nickname already exists. Please choose a different one.'
            return render_template('registration.html', error=True,
                                   error_message=error_message)
        else:
            database.add_user(username, password)
            return render_template('main_page.html')
    return render_template('registration.html', error=False)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
