import os
# from dotenv import load_dotenv
from flask_socketio import SocketIO, emit

from flask import Flask, render_template, request, redirect, url_for, session
# load_dotenv('enviro.env')

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
class PasswordError(Exception):
    pass

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
error_message_dict = {
    'username_create' : 'Sorry this Username is already in use',
    'password_not_match' : 'Password does not match',
    'incorrect_password' : 'Incorrect Password, Please try again',
    'User_not_found' : 'Username does not exist, Please create and account'
}
user_log_in_info = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def form_submission():
    name = request.form["name"]
    email = request.form['email']
    message = request.form['message']
    with open("form-submission.txt", 'a') as f:
        f.write(f"\n\n\n\nNew Submission\nName: {name}\nEmail: {email}\nMessage: {message}")
    return redirect(url_for('success'))


@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/account-created")
def created():
    return render_template("account-created.html")

@app.route("/store")
def store():
    return render_template("store.html")
@app.route('/account')
def account():
    return render_template("account.html")

@app.route("/create", methods=['POST'])
def create():

        username = request.form['create-username']
        password = request.form['create-password']
        confirmed_password = request.form['confirm-password']
        if password != confirmed_password:
            return render_template('account.html', message = error_message_dict['password_not_match'] )
        if username in user_log_in_info:
            return render_template('account.html', message = error_message_dict['username_create'] )

        username = Account(username,password)
        user_log_in_info[username.username] = username.password
        return redirect(url_for('created'))

@app.route("/store", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username not in user_log_in_info:
        return render_template('store.html', message = error_message_dict['User_not_found'])
    if password != user_log_in_info.get(username):
        return render_template('store.html', message = error_message_dict['incorrect_password'])
    session['username'] = username
    return redirect(url_for('store'))






@app.route("/store/blackcastle")
def blackcastle():
    return render_template("/store-item-1.html")

@app.route("/store/faces")
def faces():
    return render_template("/store-item-2.html")

@app.route("/store/lake")
def lake():
    return render_template("/store-item-3.html")

@app.route("/store/sheep")
def sheep():
    return render_template("/store-item-4.html")
@app.route("/store/bmx")
def bmx():
    return render_template("/store-item-5.html")
@app.route("/store/TaSe")
def TaSe():
    return render_template("/store-item-6.html")
@app.route("/store/bird")
def bird():
    return render_template("/store-item-7.html")
@app.route("/store/lighthouse")
def lighthouse():
    return render_template("/store-item-8.html")
@app.route("/store/hills")
def hills():
    return render_template("/store-item-9.html")
@app.route("/store/evischen")
def evischen():
    return render_template("/store-item-10.html")

if __name__ == "__main__":
    app.run(debug=True, port=9101)
