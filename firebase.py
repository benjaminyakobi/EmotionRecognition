from time import sleep
from firebase_admin import db

import pyrebase

config = {
    "apiKey": "AIzaSyBkWxh3HyU8hyeGb77QrLfqei81L_mHuoA",
    "authDomain": "finalproject-50eb9.firebaseapp.com",
    "databaseURL": "https://finalproject-50eb9-default-rtdb.firebaseio.com/",
    "storageBucket": "finalproject-50eb9.appspot.com",
    "messagingSenderId": "733144331218",
    "appId": "1:733144331218:web:666bfd8ebc664f26b64e0b",
    "measurementId": "G-M61DQFC72B"
}

# initialize firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
user = auth.sign_in_with_email_and_password('a@b.cc', '000000')
print(user)
data = {'a': 1, 'b': 2}
sleep(1)
results = db.push(data)
