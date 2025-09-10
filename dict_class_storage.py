error_message_dict = {
    'username_create' : 'Sorry this Username is already in use',
    'password_not_match' : 'Password does not match',
    'incorrect_password' : 'Incorrect Password, Please try again',
    'User_not_found' : 'Username does not exist, Please create and account'
}
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
class PasswordError(Exception):
    pass
class UsernameError(Exception):
    pass

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
