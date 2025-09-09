import os
from dotenv import load_dotenv
from flask_socketio import SocketIO, emit

from flask import Flask, render_template, request, redirect, url_for, session
load_dotenv('enviro.env')

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
class PasswordError(Exception):
    pass
class UsernameError(Exception):
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

    if username not in user_log_in_info:
        return render_template('store.html', message = UsernameError(error_message_dict['User_not_found']))
    if password != user_log_in_info.get(username):
        return render_template('store.html', message = PasswordError(error_message_dict['incorrect_password']))
    session['username'] = username
    return redirect(url_for('store'))

@app.route('/logout')
def logout():
    """Logout action for the app, but still keeping the user in the login info so they can log back in if needed until the site restarts"""
    session.pop('username', None)

    return redirect(url_for('store'))

store_page_dict = {
    'blackcastle' : {
        'src_main':"../static/images/black-castle.jpg",
        'src_framed':"../static/images/blackcastle-framed.PNG",
        'alt_main':"image of the front of a pub",
        'alt_framed' : "framed image of the front of a pub",
        'name' : "BlackCastle Pub Print",
        'desc': "Print of your chosen size either framed or not framed of the front of a bar called the BlackCastle based in Wicklow Town"
    },
    'faces' : {
        'src_main':"../static/images/faces.jpg",
        'src_framed':"../static/images/faces-framed-small.PNG",
        'alt_main':"image taken of a person wearing multiple masks on a stage",
        'alt_framed' : "Framed image taken of a person wearing multiple masks on a stage",
        'name' : "Many Faces Print",
        'desc': "Print of your chosen size either framed or not framed of"
    },
    'lake' : {
        'src_main':"../static/images/lake.jpg",
        'src_framed':"../static/images/lake-framed-small.PNG",
        'alt_main':"A landscape photo of a large lake in a valley",
        'alt_framed' : "Framed landscape photo of a large lake in a valley",
        'name' : "Lakes Print",
        'desc': "Print of your chosen size either framed or not framed of"
    },
    'sheep' : {
        'src_main':"../static/images/sheep-pic.jpg",
        'src_framed':"../static/images/sheep-framed.PNG",
        'alt_main':"image of a field with three sheep in view",
        'alt_framed' : "Framed image of a field with three sheep in view",
        'name' : "Three Sheep Print",
        'desc': "Print of your chosen size either framed or not framed of"
    },
    'bmx' : {
        'src_main':"../static/images/bike.jpeg",
        'src_framed':"../static/images/bike-framed.JPG",
        'alt_main':"Image of a man doing a trick on a BMX bike",
        'alt_framed' : "Framed Image of a man doing a trick on a BMX bike",
        'name' : "BMX Stunt Print",
        'desc': "Print of your chosen size either framed or not framed of"
    },
    'TaSe' : {
        'src_main':"../static/images/pub-2.jpg",
        'src_framed':"../static/images/pub-framed.JPG",
        'alt_main':"image of the front of a pub covered in Guinness logos",
        'alt_framed' : "Framed image of the front of a pub covered in Guinness logos",
        'name' : "Tá Se's Pub Print",
        'desc': "Print of your chosen size either framed or not framed of"
    },
    'bird' : {
        'src_main':"../static/images/bird.jpg",
        'src_framed':"../static/images/bird-framed.JPG",
        'alt_main':"image of a small bird sitting on a branch",
        'alt_framed' : "Framed image of a small bird sitting on a branch",
        'name' : "Little Bird Print",
        'desc': "Print of your chosen size either framed or not framed of"
    },
    'hills' : {
        'src_main':"../static/images/fields.jpg",
        'src_framed':"../static/images/fields-framed.JPG",
        'alt_main':"image of an open field with rolling hills in the background",
        'alt_framed' : "Framed image of an open field with rolling hills in the background",
        'name' : "Rolling Hills Print",
        'desc': "Print of your chosen size either framed or not framed of"
    },
    'evischen' : {
        'src_main':"../static/images/evicshen-opium.jpg",
        'src_framed':"../static/images/evicshen-framed.JPG",
        'alt_main':"image of a musician holding a mini drum with a symbal attached about to tap it",
        'alt_framed' : "Framed image of a musician holding a mini drum with a symbal attached about to tap it",
        'name' : "Evischen at Opium Print",
        'desc': "Print of your chosen size either framed or not framed of"
    },
    'lighthouse' : {
        'src_main':"../static/images/lighthouse.jpg",
        'src_framed':"../static/images/lighthouse-framed.JPG",
        'alt_main':"image of someone jumping a gap in front of a lighthouse",
        'alt_framed' : "Framed image of someone jumping a gap in front of a lighthouse",
        'name' : "Lighthouse Jump Print",
        'desc': "Print of your chosen size either framed or not framed of"
    },
}




@app.route("/store/blackcastle")
def blackcastle():
    return render_template("/store-item.html", src_main = store_page_dict['blackcastle']['src_main'],src_framed=store_page_dict['blackcastle']['src_framed'], alt_main = store_page_dict['blackcastle']['alt_main'], alt_framed = store_page_dict['blackcastle']['alt_framed'],name= store_page_dict['blackcastle']['name'], desc = store_page_dict['blackcastle']['desc'] )
@app.route("/store/faces")
def faces():
    return render_template("/store-item.html", src_main = store_page_dict['faces']['src_main'],src_framed=store_page_dict['faces']['src_framed'], alt_main = store_page_dict['faces']['alt_main'], alt_framed = store_page_dict['faces']['alt_framed'],name= store_page_dict['faces']['name'], desc = store_page_dict['faces']['desc'] )
@app.route("/store/lake")
def lake():
    return render_template("/store-item.html", src_main = store_page_dict['lake']['src_main'],src_framed=store_page_dict['lake']['src_framed'], alt_main = store_page_dict['lake']['alt_main'], alt_framed = store_page_dict['lake']['alt_framed'],name= store_page_dict['lake']['name'], desc = store_page_dict['lake']['desc'] )
@app.route("/store/sheep")
def sheep():
    return render_template("/store-item.html", src_main = store_page_dict['sheep']['src_main'],src_framed=store_page_dict['sheep']['src_framed'], alt_main = store_page_dict['sheep']['alt_main'], alt_framed = store_page_dict['sheep']['alt_framed'],name= store_page_dict['sheep']['name'], desc = store_page_dict['sheep']['desc'] )
@app.route("/store/bmx")
def bmx():
    return render_template("/store-item.html", src_main = store_page_dict['bmx']['src_main'],src_framed=store_page_dict['bmx']['src_framed'], alt_main = store_page_dict['bmx']['alt_main'], alt_framed = store_page_dict['bmx']['alt_framed'],name= store_page_dict['bmx']['name'], desc = store_page_dict['bmx']['desc'] )
@app.route("/store/TaSe")
def TaSe():
    return render_template("/store-item.html", src_main = store_page_dict['TaSe']['src_main'],src_framed=store_page_dict['TaSe']['src_framed'], alt_main = store_page_dict['TaSe']['alt_main'], alt_framed = store_page_dict['TaSe']['alt_framed'],name= store_page_dict['TaSe']['name'], desc = store_page_dict['TaSe']['desc'] )
@app.route("/store/bird")
def bird():
    return render_template("/store-item.html", src_main = store_page_dict['bird']['src_main'],src_framed=store_page_dict['bird']['src_framed'], alt_main = store_page_dict['bird']['alt_main'], alt_framed = store_page_dict['bird']['alt_framed'],name= store_page_dict['bird']['name'], desc = store_page_dict['bird']['desc'] )
@app.route("/store/lighthouse")
def lighthouse():
    return render_template("/store-item.html", src_main = store_page_dict['lighthouse']['src_main'],src_framed=store_page_dict['lighthouse']['src_framed'], alt_main = store_page_dict['lighthouse']['alt_main'], alt_framed = store_page_dict['lighthouse']['alt_framed'],name= store_page_dict['lighthouse']['name'], desc = store_page_dict['lighthouse']['desc'] )
@app.route("/store/hills")
def hills():
    return render_template("/store-item.html", src_main = store_page_dict['hills']['src_main'],src_framed=store_page_dict['hills']['src_framed'], alt_main = store_page_dict['hills']['alt_main'], alt_framed = store_page_dict['hills']['alt_framed'],name= store_page_dict['hills']['name'], desc = store_page_dict['hills']['desc'] )
@app.route("/store/evischen")
def evischen():
    return render_template("/store-item.html", src_main = store_page_dict['evischen']['src_main'],src_framed=store_page_dict['evischen']['src_framed'], alt_main = store_page_dict['evischen']['alt_main'], alt_framed = store_page_dict['evischen']['alt_framed'],name= store_page_dict['evischen']['name'], desc = store_page_dict['evischen']['desc'] )

if __name__ == "__main__":
    app.run(debug=True, port=9101)
