from flask import Flask, request, render_template, redirect, url_for
import database
import dota_db

app = Flask(__name__)
is_authorized = False
user_id = None

@app.route('/', methods=['GET', 'POST'])
def main():
    if is_authorized:
        return render_template('main_page.html', error=False, is_authorized="true")
    else:
        return render_template('main_page.html', error=False, is_authorized="false")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = database.get_dictionary_of_users()
        if username in users and users[username][0] == password:
            global is_authorized
            is_authorized = True
            global user_id
            user_id = database.get_user_id_by_login(username)
            return redirect(url_for('choose'))  # Redirect to the choose page after successful login
        else:
            error_message = 'Incorrect username or password. Please try again.'
            return render_template('login.html', error=True, error_message=error_message)
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
            return render_template('registration.html', error=True, error_message=error_message)
        else:
            database.add_user(username, password)
            global user_id
            user_id = database.get_user_id_by_login(username)
            global is_authorized
            is_authorized = True
            return redirect(url_for('main'))  # Redirect to the main page after successful registration
    return render_template('registration.html', error=False)

@app.route('/choose', methods=['GET', 'POST'])
def choose():
    if is_authorized:
        return render_template('choose_desteny.html')
    else:
        return redirect(url_for('login'))  # Redirect to the login page if not authorized

@app.route('/dota2', methods=['GET', 'POST'])
def dota2():
    if is_authorized:
        dota_applications = dota_db.get_dictionary_of_quest()
        return render_template('dota.html', dota_applications=dota_applications)
    else:
        return redirect(url_for('login'))

@app.route('/add_application', methods=['POST'])
def add_application():
    if is_authorized:
        if request.method == 'POST':
            user_nickname = request.form['name']
            user_MMR = int(request.form['rating'])
            user_comment = request.form['comment']
            user_pos = request.form['position']
            dota_db.add_application(user_id, user_MMR, user_nickname, user_comment, user_pos)
            return redirect(url_for('dota2'))
    else:
        return redirect(url_for('login'))


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template('chat_base.html')


@app.route('/all_chats', methods=['GET', 'POST'])
def all_chats():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
