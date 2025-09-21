import os
from dotenv import load_dotenv
import random
from models import error_message_dict, PasswordError, UsernameError, Account, blackcastle, faces, lake, sheep, bmx, TaSe,evischen,lighthouse,hills,bird
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
    try:
        '''
        This is here to make sure that when you are logged in and go onto the store page
        it will display the random message
        '''
        username = session['username']

        welcome_templates = [
        f"Welcome back to our store, {username.title()}! Ready to shop?",
        f"Hey {username.title()}, great to see you again! Check out our latest deals.",
        f"Hello {username.title()}! Your cart is waiting for you.",
        f"Hi {username.title()}, we've missed you! Discover new arrivals today.",
        f"Glad you're here, {username.title()}! Enjoy exclusive member offers." ,
        f"Welcome, {username.title()}! Let's find something special for you.",
        f"Hey {username.title()}, your favorite products are just a click away.",
        f"Good to see you, {username.title()}! Don't miss our flash sales.",
        f"Yo {username.title()}, ready to treat yourself?",
        f"Hi {username.title()}! Shop the best deals just for you.",
        f"Welcome, {username.title()}! We have new recommendations for you.",
        f"Hey {username.title()}, your wishlist items are on sale!",
        f"Hello {username.title()}! Find your next favorite product.",
        f"Hi {username.title()}, exclusive discounts await you.",
        f"Glad to see you, {username.title()}! Check out trending items.",
        f"Welcome back, {username.title()}! Your loyalty means a lot.",
        f"Hey {username.title()}, discover top-rated products today.",
        f"Hello {username.title()}! Your shopping adventure starts here.",
        f"Hi {username.title()}, don't forget to use your reward points.",
        f"Welcome, {username.title()}! Enjoy free shipping on select items.",
        f"Hey {username.title()}, new arrivals just landed.",
        f"Good to see you, {username.title()}! Shop with confidence.",
        f"Yo {username.title()}, your personalized deals are ready.",
        f"Hi {username.title()}! Save big on your favorite brands.",
        f"Welcome, {username.title()}! Your feedback helps us improve.",
        f"Hey {username.title()}, shop now and earn bonus points.",
        f"Hello {username.title()}! Limited-time offers just for you.",
        f"Hi {username.title()}, explore our bestsellers.",
        f"Glad you're here, {username.title()}! Enjoy hassle-free returns.",
        f"Welcome back, {username.title()}! Your last order was a hit.",
        f"Hey {username.title()}, get inspired by our collections.",
        f"Hello {username.title()}! Your next purchase could be free.",
        f"Hi {username.title()}, refer a friend and save more.",
        f"Welcome, {username.title()}! Shop eco-friendly products.",
        f"Hey {username.title()}, your style, your store.",
        f"Good to see you, {username.title()}! Shop by category.",
        f"Yo {username.title()}, flash deals are live now.",
        f"Hi {username.title()}! Your opinion matters to us.",
        f"Welcome, {username.title()}! Shop with exclusive coupons.",
        f"Hey {username.title()}, your favorite items are restocked.",
        f"Hello {username.title()}! Enjoy seamless checkout.",
        f"Hi {username.title()}, discover new brands today.",
        f"Glad to see you, {username.title()}! Shop trending now.",
        f"Welcome back, {username.title()}! Your shopping journey continues.",
        f"Hey {username.title()}, unlock special rewards.",
        f"Hello {username.title()}! Shop with confidence.",
        f"Hi {username.title()}, your cart is waiting for you.",
        f"Welcome, {username.title()}! Find something unique.",
        f"Hey {username.title()}, shop the latest collections.",
        f"Good to see you, {username.title()}! Enjoy member-only perks.",
        f"Yo {username.title()}, your next order ships free.",
        f"Hi {username.title()}! Shop and save today.",
        ]
        return render_template('store.html', log_in_message = str(random.choice(welcome_templates)))
    except:
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
      the usernames to see if it exists and then checks to make sure the password is correct if all is correct
      it will take the username and input it into a random welcome message to display on the store page """
    username = request.form['username']
    password = request.form['password']
    welcome_templates = [
        f"Welcome back to our store, {username.title()}! Ready to shop?",
        f"Hey {username.title()}, great to see you again! Check out our latest deals.",
        f"Hello {username.title()}! Your cart is waiting for you.",
        f"Hi {username.title()}, we've missed you! Discover new arrivals today.",
        f"Glad you're here, {username.title()}! Enjoy exclusive member offers." ,
        f"Welcome, {username.title()}! Let's find something special for you.",
        f"Hey {username.title()}, your favorite products are just a click away.",
        f"Good to see you, {username.title()}! Don't miss our flash sales.",
        f"Yo {username.title()}, ready to treat yourself?",
        f"Hi {username.title()}! Shop the best deals just for you.",
        f"Welcome, {username.title()}! We have new recommendations for you.",
        f"Hey {username.title()}, your wishlist items are on sale!",
        f"Hello {username.title()}! Find your next favorite product.",
        f"Hi {username.title()}, exclusive discounts await you.",
        f"Glad to see you, {username.title()}! Check out trending items.",
        f"Welcome back, {username.title()}! Your loyalty means a lot.",
        f"Hey {username.title()}, discover top-rated products today.",
        f"Hello {username.title()}! Your shopping adventure starts here.",
        f"Hi {username.title()}, don't forget to use your reward points.",
        f"Welcome, {username.title()}! Enjoy free shipping on select items.",
        f"Hey {username.title()}, new arrivals just landed.",
        f"Good to see you, {username.title()}! Shop with confidence.",
        f"Yo {username.title()}, your personalized deals are ready.",
        f"Hi {username.title()}! Save big on your favorite brands.",
        f"Welcome, {username.title()}! Your feedback helps us improve.",
        f"Hey {username.title()}, shop now and earn bonus points.",
        f"Hello {username.title()}! Limited-time offers just for you.",
        f"Hi {username.title()}, explore our bestsellers.",
        f"Glad you're here, {username.title()}! Enjoy hassle-free returns.",
        f"Welcome back, {username.title()}! Your last order was a hit.",
        f"Hey {username.title()}, get inspired by our collections.",
        f"Hello {username.title()}! Your next purchase could be free.",
        f"Hi {username.title()}, refer a friend and save more.",
        f"Welcome, {username.title()}! Shop eco-friendly products.",
        f"Hey {username.title()}, your style, your store.",
        f"Good to see you, {username.title()}! Shop by category.",
        f"Yo {username.title()}, flash deals are live now.",
        f"Hi {username.title()}! Your opinion matters to us.",
        f"Welcome, {username.title()}! Shop with exclusive coupons.",
        f"Hey {username.title()}, your favorite items are restocked.",
        f"Hello {username.title()}! Enjoy seamless checkout.",
        f"Hi {username.title()}, discover new brands today.",
        f"Glad to see you, {username.title()}! Shop trending now.",
        f"Welcome back, {username.title()}! Your shopping journey continues.",
        f"Hey {username.title()}, unlock special rewards.",
        f"Hello {username.title()}! Shop with confidence.",
        f"Hi {username.title()}, your cart is waiting for you.",
        f"Welcome, {username.title()}! Find something unique.",
        f"Hey {username.title()}, shop the latest collections.",
        f"Good to see you, {username.title()}! Enjoy member-only perks.",
        f"Yo {username.title()}, your next order ships free.",
        f"Hi {username.title()}! Shop and save today.",
        ]

    if username not in user_log_in_info:
        return render_template('store.html', message = UsernameError(error_message_dict['User_not_found']))
    if password != user_log_in_info.get(username):
        return render_template('store.html', message = PasswordError(error_message_dict['incorrect_password']))
    session['username'] = username

    return render_template('store.html', log_in_message = str(random.choice(welcome_templates)))

@app.route('/logout')
def logout():
    """Logout action for the app, but still keeping the user in the
    login info so they can log back in if needed until the site restarts"""
    session.pop('username', None)

    return redirect(url_for('store'))
'''
All of the bellow is for rendering each store page taking each Store_Item and applying them to the html with
the help of render_template and jinja so there is only the need for one html page for
the store items rather than 10
'''
@app.route("/store/blackcastle")
def blackcastle_page():
    return render_template("/store-item.html", src_main = blackcastle.img,src_framed=blackcastle.secondary, alt_main = blackcastle.alt, alt_framed = blackcastle.alt_secondary,name= blackcastle.name, desc = blackcastle.desc )
@app.route("/store/faces")
def faces_page():
    return render_template("/store-item.html", src_main = faces.img,src_framed=faces.secondary, alt_main = faces.alt, alt_framed = faces.alt_secondary,name= faces.name, desc = faces.desc )
@app.route("/store/lake")
def lake_page():
    return render_template("/store-item.html", src_main = lake.img, src_framed = lake.secondary, alt_main = lake.alt, alt_framed = lake.alt_secondary ,name = lake.name, desc = lake.desc )
@app.route("/store/sheep")
def sheep_page():
    return render_template("/store-item.html", src_main = sheep.img,src_framed=sheep.secondary, alt_main = sheep.alt, alt_framed = sheep.secondary,name= sheep.name, desc = sheep.desc )
@app.route("/store/bmx")
def bmx_page():
    return render_template("/store-item.html", src_main = bmx.img,src_framed=bmx.secondary, alt_main = bmx.alt, alt_framed = bmx.alt_secondary,name= bmx.name, desc = bmx.desc )
@app.route("/store/TaSe")
def TaSe_page():
    return render_template("/store-item.html", src_main = TaSe.img,src_framed=TaSe.secondary, alt_main = TaSe.alt, alt_framed = TaSe.alt_secondary,name= TaSe.name, desc = TaSe.desc )
@app.route("/store/bird")
def bird_page():
    return render_template("/store-item.html", src_main = bird.img,src_framed=bird.secondary, alt_main = bird.alt, alt_framed = bird.alt_secondary,name= bird.name, desc = bird.desc )
@app.route("/store/lighthouse")
def lighthouse_page():
    return render_template("/store-item.html", src_main = lighthouse.img,src_framed=lighthouse.secondary, alt_main = lighthouse.alt, alt_framed = lighthouse.alt_secondary,name= lighthouse.name, desc = lighthouse.desc )
@app.route("/store/hills")
def hills_page():
    return render_template("/store-item.html", src_main = hills.img,src_framed=hills.secondary, alt_main = hills.alt, alt_framed = hills.alt_secondary,name= hills.name, desc = hills.desc )
@app.route("/store/evischen")
def evischen_page():
    return render_template("/store-item.html", src_main = evischen.img,src_framed=evischen.secondary, alt_main = evischen.alt, alt_framed = evischen.alt_secondary,name= evischen.name, desc = evischen.desc )





if __name__ == "__main__":
    app.run(debug=True, port=9101)
