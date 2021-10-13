from pyrebase import pyrebase
from Screens import LoginRegister

if __name__ == '__main__':
    config = {
        'apiKey': "AIzaSyBkWxh3HyU8hyeGb77QrLfqei81L_mHuoA",
        'authDomain': "finalproject-50eb9.firebaseapp.com",
        'databaseURL': "https://finalproject-50eb9-default-rtdb.firebaseio.com",
        'projectId': "finalproject-50eb9",
        'storageBucket': "finalproject-50eb9.appspot.com",
        'messagingSenderId': "733144331218",
        'appId': "1:733144331218:web:666bfd8ebc664f26b64e0b",
        'measurementId': "G-M61DQFC72B"
    }

    # initialize firebase
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    db = firebase.database()

    # Initialze person as dictionary
    user = {"is_logged_in": False, "name": "", "email": "", "uid": ""}

    user = LoginRegister.main_account_screen(firebase)
