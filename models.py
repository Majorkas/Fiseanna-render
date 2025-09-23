import random

def welcome(username):
    '''Function for creating the random welcome template (templates written by chatgpt)'''
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
    return random.choice(welcome_templates)

error_message_dict = {
    'username_create' : 'Sorry this Username is already in use',
    'password_not_match' : 'Password does not match',
    'incorrect_password' : 'Incorrect Password, Please try again',
    'User_not_found' : 'Username does not exist, Please create an account'
}

class PasswordError(Exception):
    pass
class UsernameError(Exception):
    pass
class InputError(Exception):
    pass

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Store_Item:
    def __init__(self,img,secondary,alt,alt_secondary,name,desc,price,stock,):
        self.img = img
        self.secondary = secondary
        self.alt = alt
        self.alt_secondary = alt_secondary
        self.name = name
        self.desc = desc
        self.price = price
        self.stock = stock

    def minus_stock(self, amount):
     if self.stock < amount:
        return InputError('Not Enough Stock Available')
     else:
        self.stock -= int(amount)
        return self.stock
    def add_stock(self, amount):
     self.stock += int(amount)
     return self.stock
    def __str__(self):
        return f"{self.name} a {self.desc} costing {self.price}"
    def __repr__(self):
        return f"Main img url : {self.img}, Secondary Image Url : {self.secondary},Main Alt Text: {self.alt},Secondary Alt Text : {self.alt_secondary}, Item Name : {self.name}, Item Description : {self.desc}, Item Price : {self.price}, Remaining stock : {self.stock} "

blackcastle = Store_Item(
    "../static/images/black-castle.jpg",
    "../static/images/blackcastle-framed.PNG",
    "image of the front of a pub","framed image of the front of a pub",
    "BlackCastle Pub Print",
    "Print of your chosen size either framed or not framed of the front of a bar called the BlackCastle based in Wicklow Town",
    13,
    1,
    )
faces = Store_Item(
    "../static/images/faces.jpg",
    "../static/images/faces-framed-small.PNG",
    "image taken of a person wearing multiple masks on a stage",
    "Framed image taken of a person wearing multiple masks on a stage",
    "Many Faces Print",
    "Print of your chosen size either framed or not framed of a person wearing multiple masks on a stage",
    13,
    1,
    )
lake = Store_Item(
    "../static/images/lake.jpg",
    "../static/images/lake-framed-small.PNG",
    "A landscape photo of a large lake in a valley",
    "Framed landscape photo of a large lake in a valley",
    "Lakes Print",
    "Print of your chosen size either framed or not framed of a large lake in a valley",
    13,
    1,
    )
sheep = Store_Item(
    "../static/images/sheep-pic.jpg",
    "../static/images/sheep-framed.PNG",
    "image of a field with three sheep in view",
    "Framed image of a field with three sheep in view",
    "Three Sheep Print",
    "Print of your chosen size either framed or not framed ofa field with three sheep in view",
    13,
    1,
    )
bmx = Store_Item(
    "../static/images/bike.jpeg",
    "../static/images/bike-framed.JPG",
    "Image of a man doing a trick on a BMX bike",
    "Framed Image of a man doing a trick on a BMX bike",
    "BMX Stunt Print",
    "Print of your chosen size either framed or not framed of a man doing a trick on a BMX bike",
    13,
    1,
    )
TaSe = Store_Item(
    "../static/images/pub-2.jpg",
    "../static/images/pub-framed.JPG",
    "image of the front of a pub covered in Guinness logos",
    "Framed image of the front of a pub covered in Guinness logos",
    "Tá Se's Pub Print",
    "Print of your chosen size either framed or not framed of the front of a pub covered in Guinness logos",
    13,
    1,
    )
bird = Store_Item(
    "../static/images/bird.jpg",
    "../static/images/bird-framed.JPG",
    "image of a small bird sitting on a branch",
    "Framed image of a small bird sitting on a branch",
    "Little Bird Print",
    "Print of your chosen size either framed or not framed of a small bird sitting on a branch",
    13,
    1,
    )
hills = Store_Item(
    "../static/images/fields.jpg",
    "../static/images/fields-framed.JPG",
    "image of an open field with rolling hills in the background",
    "Framed image of an open field with rolling hills in the background",
    "Rolling Hills Print",
    "Print of your chosen size either framed or not framed of an open field with rolling hills in the background",
    13,
    1,
    )
evischen = Store_Item(
    "../static/images/evicshen-opium.jpg",
    "../static/images/evicshen-framed.JPG",
    "image of a musician holding a mini drum with a symbal attached about to tap it",
    "Framed image of a musician holding a mini drum with a symbal attached about to tap it",
    "Evischen at Opium Print",
    "Print of your chosen size either framed or not framed of a musician holding a mini drum with a symbal attached about to tap it",
    13,
    1,
    )
lighthouse = Store_Item(
    "../static/images/lighthouse.jpg",
    "../static/images/lighthouse-framed.JPG",
    "image of someone jumping a gap in front of a lighthouse",
    "Framed image of someone jumping a gap in front of a lighthouse",
    "Lighthouse Jump Print",
    "Print of your chosen size either framed or not framed of someone jumping a gap in front of a lighthouse",
    13,
    1,
    )
