
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
    def __init__(self,img,secondary,alt,alt_secondary,name,desc,price,stock,page):
        self.img = img
        self.secondary = secondary
        self.alt = alt
        self.alt_secondary = alt_secondary
        self.name = name
        self.desc = desc
        self.price = price
        self.stock = stock
        self.page = page

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
    "blackcastle")
faces = Store_Item(
    "../static/images/faces.jpg",
    "../static/images/faces-framed-small.PNG",
    "image taken of a person wearing multiple masks on a stage",
    "Framed image taken of a person wearing multiple masks on a stage",
    "Many Faces Print",
    "Print of your chosen size either framed or not framed of",
    13,
    1,
    "faces")
lake = Store_Item(
    "../static/images/lake.jpg",
    "../static/images/lake-framed-small.PNG",
    "A landscape photo of a large lake in a valley",
    "Framed landscape photo of a large lake in a valley",
    "Lakes Print",
    "Print of your chosen size either framed or not framed of",
    13,
    1,
    "lake")
sheep = Store_Item(
    "../static/images/sheep-pic.jpg",
    "../static/images/sheep-framed.PNG",
    "image of a field with three sheep in view",
    "Framed image of a field with three sheep in view",
    "Three Sheep Print",
    "Print of your chosen size either framed or not framed of",
    13,
    1,
    "sheep"
)
bmx = Store_Item(
    "../static/images/bike.jpeg",
    "../static/images/bike-framed.JPG",
    "Image of a man doing a trick on a BMX bike",
    "Framed Image of a man doing a trick on a BMX bike",
    "BMX Stunt Print",
    "Print of your chosen size either framed or not framed of",
    13,
    1,
    "bmx")
TaSe = Store_Item(
    "../static/images/pub-2.jpg",
    "../static/images/pub-framed.JPG",
    "image of the front of a pub covered in Guinness logos",
    "Framed image of the front of a pub covered in Guinness logos",
    "Tá Se's Pub Print",
    "Print of your chosen size either framed or not framed of",
    13,
    1,
    "TaSe")
bird = Store_Item(
    "../static/images/bird.jpg",
    "../static/images/bird-framed.JPG",
    "image of a small bird sitting on a branch",
    "Framed image of a small bird sitting on a branch",
    "Little Bird Print",
    "Print of your chosen size either framed or not framed of",
    13,
    1,
    "bird")
hills = Store_Item(
    "../static/images/fields.jpg",
    "../static/images/fields-framed.JPG",
    "image of an open field with rolling hills in the background",
    "Framed image of an open field with rolling hills in the background",
    "Rolling Hills Print",
    "Print of your chosen size either framed or not framed of",
    13,
    1,
    "hills")
evischen = Store_Item(
    "../static/images/evicshen-opium.jpg",
    "../static/images/evicshen-framed.JPG",
    "image of a musician holding a mini drum with a symbal attached about to tap it",
    "Framed image of a musician holding a mini drum with a symbal attached about to tap it",
    "Evischen at Opium Print",
    "Print of your chosen size either framed or not framed of",
    13,
    1,
    "evischen")
lighthouse = Store_Item(
    "../static/images/lighthouse.jpg",
    "../static/images/lighthouse-framed.JPG",
    "image of someone jumping a gap in front of a lighthouse",
    "Framed image of someone jumping a gap in front of a lighthouse",
    "Lighthouse Jump Print",
    "Print of your chosen size either framed or not framed of",
    13,
    1,
    "lighthouse")
