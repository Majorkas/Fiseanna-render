import os
from dotenv import load_dotenv
import random
from dict_class_storage import error_message_dict, store_page_dict, PasswordError, UsernameError, Account, blackcastle, faces, lake
from flask import Flask, render_template, request, redirect, url_for, session
load_dotenv('enviro.env')

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

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
    if session['username']:
        username = session['username']
        welcome_templates = [
        f"Welcome back to our store, {username.title()}! Ready to shop?",
        f"Hey {username.title()}, great to see you again! Check out our latest deals.",
        f"Hello {username.title()}! Your cart is waiting for you.",
        f"Hi {username.title()}, we've missed you! Discover new arrivals today.",
        f"Glad you're here, {username.title()}! Enjoy exclusive member offers.",
        f"Welcome, {username.title()}! Let's find something special for you.",
        f"Hey {username.title()}, your favorite products are just a click away.",
        f"Good to see you, {username.title()}! Don't miss our flash sales.",
        f"Yo {username.title()}, ready to treat yourself?",
        f"Hi {username.title()}! Shop the best deals just for you."
        ]
        return render_template('store.html', log_in_message = str(random.choice(welcome_templates)))
    return render_template("store.html")
@app.route('/account')
def account():
    return render_template("account.html")

@app.route("/create", methods=['POST'])
def create():
        """Used to create an account taking the form inputs checking if the username is already present in the dict and seeing if the
        password and confirm password inputs match finally returning a success page if all if good"""

        username = request.form['create-username']
        password = request.form['create-password']
        confirmed_password = request.form['confirm-password']
        if password != confirmed_password:
            return render_template('account.html', message = PasswordError(error_message_dict['password_not_match']) )
        if username in user_log_in_info:
            return render_template('account.html', message = UsernameError(error_message_dict['username_create']) )

        username = Account(username,password)
        user_log_in_info[username.username] = username.password
        return redirect(url_for('created'))

@app.route("/store", methods=['POST'])
def login():
    """ log-in action for the site takes the username and password and checks it against the dict storing all
      the usernames to see if it exists and then checks to make sure the password is correct """
    username = request.form['username']
    password = request.form['password']
    welcome_templates = [
    f"Welcome back to our store, {username.title()}! Ready to shop?",
    f"Hey {username.title()}, great to see you again! Check out our latest deals.",
    f"Hello {username.title()}! Your cart is waiting for you.",
    f"Hi {username.title()}, we've missed you! Discover new arrivals today.",
    f"Glad you're here, {username.title()}! Enjoy exclusive member offers.",
    f"Welcome, {username.title()}! Let's find something special for you.",
    f"Hey {username.title()}, your favorite products are just a click away.",
    f"Good to see you, {username.title()}! Don't miss our flash sales.",
    f"Yo {username.title()}, ready to treat yourself?",
    f"Hi {username.title()}! Shop the best deals just for you."
]

    if username not in user_log_in_info:
        return render_template('store.html', message = UsernameError(error_message_dict['User_not_found']))
    if password != user_log_in_info.get(username):
        return render_template('store.html', message = PasswordError(error_message_dict['incorrect_password']))
    session['username'] = username
    return render_template('store.html', log_in_message = str(random.choice(welcome_templates)))

@app.route('/logout')
def logout():
    """Logout action for the app, but still keeping the user in the login info so they can log back in if needed until the site restarts"""
    session.pop('username', None)

    return redirect(url_for('store'))

'''
All of the bellow is for rendering each store page taking the needed src and alts from the imported store_page_dict and applying them to the html with the help of render_template and jinja so there is only the need for one html page for the store items rather than 10
'''
@app.route("/store/blackcastle")
def blackcastle_page():
    return render_template("/store-item.html", src_main = blackcastle.img,src_framed=blackcastle.secondary, alt_main = blackcastle.alt, alt_framed = blackcastle.alt_secondary,name= blackcastle.name, desc = blackcastle.desc )
@app.route("/store/faces")
def faces_page():
    return render_template("/store-item.html", src_main = store_page_dict['faces']['src_main'],src_framed=store_page_dict['faces']['src_framed'], alt_main = store_page_dict['faces']['alt_main'], alt_framed = store_page_dict['faces']['alt_framed'],name= store_page_dict['faces']['name'], desc = store_page_dict['faces']['desc'] )
@app.route("/store/lake")
def lake_page():
    return render_template("/store-item.html", src_main = store_page_dict['lake']['src_main'],src_framed=store_page_dict['lake']['src_framed'], alt_main = store_page_dict['lake']['alt_main'], alt_framed = store_page_dict['lake']['alt_framed'],name= store_page_dict['lake']['name'], desc = store_page_dict['lake']['desc'] )
@app.route("/store/sheep")
def sheep_page():
    return render_template("/store-item.html", src_main = store_page_dict['sheep']['src_main'],src_framed=store_page_dict['sheep']['src_framed'], alt_main = store_page_dict['sheep']['alt_main'], alt_framed = store_page_dict['sheep']['alt_framed'],name= store_page_dict['sheep']['name'], desc = store_page_dict['sheep']['desc'] )
@app.route("/store/bmx")
def bmx_page():
    return render_template("/store-item.html", src_main = store_page_dict['bmx']['src_main'],src_framed=store_page_dict['bmx']['src_framed'], alt_main = store_page_dict['bmx']['alt_main'], alt_framed = store_page_dict['bmx']['alt_framed'],name= store_page_dict['bmx']['name'], desc = store_page_dict['bmx']['desc'] )
@app.route("/store/TaSe")
def TaSe_page():
    return render_template("/store-item.html", src_main = store_page_dict['TaSe']['src_main'],src_framed=store_page_dict['TaSe']['src_framed'], alt_main = store_page_dict['TaSe']['alt_main'], alt_framed = store_page_dict['TaSe']['alt_framed'],name= store_page_dict['TaSe']['name'], desc = store_page_dict['TaSe']['desc'] )
@app.route("/store/bird")
def bird_page():
    return render_template("/store-item.html", src_main = store_page_dict['bird']['src_main'],src_framed=store_page_dict['bird']['src_framed'], alt_main = store_page_dict['bird']['alt_main'], alt_framed = store_page_dict['bird']['alt_framed'],name= store_page_dict['bird']['name'], desc = store_page_dict['bird']['desc'] )
@app.route("/store/lighthouse")
def lighthouse_page():
    return render_template("/store-item.html", src_main = store_page_dict['lighthouse']['src_main'],src_framed=store_page_dict['lighthouse']['src_framed'], alt_main = store_page_dict['lighthouse']['alt_main'], alt_framed = store_page_dict['lighthouse']['alt_framed'],name= store_page_dict['lighthouse']['name'], desc = store_page_dict['lighthouse']['desc'] )
@app.route("/store/hills")
def hills_page():
    return render_template("/store-item.html", src_main = store_page_dict['hills']['src_main'],src_framed=store_page_dict['hills']['src_framed'], alt_main = store_page_dict['hills']['alt_main'], alt_framed = store_page_dict['hills']['alt_framed'],name= store_page_dict['hills']['name'], desc = store_page_dict['hills']['desc'] )
@app.route("/store/evischen")
def evischen_page():
    return render_template("/store-item.html", src_main = store_page_dict['evischen']['src_main'],src_framed=store_page_dict['evischen']['src_framed'], alt_main = store_page_dict['evischen']['alt_main'], alt_framed = store_page_dict['evischen']['alt_framed'],name= store_page_dict['evischen']['name'], desc = store_page_dict['evischen']['desc'] )





if __name__ == "__main__":
    app.run(debug=True, port=9101)
