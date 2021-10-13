import json
from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
import requests
from Screens import ChangeMoviePreference
from Screens import MainScreen
from PyQt5 import QtWidgets


def center(toplevel):
    toplevel.update_idletasks()
    # Tkinter way to find the screen resolution
    # screen_width = toplevel.winfo_screenwidth()
    # screen_height = toplevel.winfo_screenheight()
    # QtWidgets way to find the screen resolution
    app = QtWidgets.QApplication([])
    screen_width = app.desktop().screenGeometry().width()
    screen_height = app.desktop().screenGeometry().height()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width / 2 - size[0] / 2
    y = screen_height / 2 - size[1] / 2
    toplevel.geometry("+%d+%d" % (x, y))


# Designing window for registration
def register(auth):
    global register_screen
    main_screen.withdraw()
    register_screen = Toplevel(main_screen)
    center(register_screen)
    register_screen.title("Register")
    register_screen.geometry("400x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(register_screen, font=("David", 16), text="Please Enter Details To Register").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, font=("David", 14), text="Email * ")
    username_lable.pack()
    username_entry = Entry(register_screen, font=("David", 14), textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, font=("David", 14), text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, font=("David", 14), textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    ttk.Button(register_screen, text="Register", width=10,
               command=lambda: register_user(auth)).place(x=100, y=200)
    ttk.Button(register_screen, text="Back", width=10,
               command=back_rgister, style='danger.TButton').place(x=200, y=200)


# Designing window for login

def login(auth):
    global login_screen
    main_screen.withdraw()
    login_screen = Toplevel(main_screen)
    login_screen.protocol('WM_DELETE_WINDOW', main_screen.destroy)

    center(login_screen)
    login_screen.title("Login")
    login_screen.geometry("400x250")
    Label(login_screen, text="Please Enter Details Below To Login", font=("David", 16)).pack()
    Label(login_screen, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Email * ", font=("David", 14)).pack()
    username_login_entry = Entry(login_screen, font=("David", 14), textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ", font=("David", 14)).pack()
    password_login_entry = Entry(login_screen, font=("David", 14), textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    ttk.Button(login_screen, text="Login", width=10,
               command=lambda: login_verify(auth)).place(x=100, y=200)
    ttk.Button(login_screen, text="Back", width=10, style='danger.TButton'
               , command=back_login).place(x=200, y=200)


def register_user(auth):
    username_info = username.get()
    password_info = password.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    try:
        auth.create_user_with_email_and_password(username_info, password_info)
        user = auth.sign_in_with_email_and_password(username_info, password_info)
        register_screen.withdraw()
        register_sucess(user, fire_base.database())


    except requests.HTTPError as e:
        register_fail(e)


# Implementing event on login button
def login_verify(firebase):
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    auth = firebase.auth()
    try:
        user = auth.sign_in_with_email_and_password(username1, password1)
        login_screen.destroy()
        # hide it by the withdraw() method of the root window.
        # make the window visible again by the deiconify() (or wm_deiconify()) method.
        main_screen.withdraw()
        MainScreen.mainMenu(user, firebase)
        # login_sucess()
    except:

        login_fail()


def login_fail():
    global login_fail_screen
    login_fail_screen = Toplevel(login_screen)
    center(login_fail_screen)
    login_fail_screen.title("Login Failed")
    # login_fail_screen.geometry("400x300")
    Label(login_fail_screen, font=("David", 16), text="Wrong email or password", bg="red").pack()
    Button(login_fail_screen, font=("David", 16), text="OK", command=delete_login_fail).pack()


def register_sucess(user, firebase):
    global register_success_screen
    register_success_screen = Toplevel(register_screen)
    center(register_success_screen)
    register_success_screen.title("Registration completed")
    # register_success_screen.geometry("400x300")
    Label(register_success_screen, font=("David", 16), text="Registration Success").pack()
    Button(register_success_screen, font=("David", 16), text="OK",
           command=lambda: delete_register_success(user, firebase)).pack()


def register_fail(e):
    global register_fail_screen
    register_fail_screen = Toplevel(register_screen)
    center(register_fail_screen)
    error_json = e.args[1]
    error = json.loads(error_json)['error']['message']
    error = error.replace("_", ' ')
    error = error.title()
    register_fail_screen.title("Error")
    # register_fail_screen.geometry("150x100")
    Label(register_fail_screen, font=("David", 16), text=error, bg="red").pack()
    Button(register_fail_screen, font=("David", 16), text="OK", command=delete_register_fail).pack()


def back_rgister():
    register_screen.destroy()
    main_screen.deiconify()


def back_login():
    login_screen.destroy()
    main_screen.deiconify()


def delete_login_fail():
    login_fail_screen.destroy()


def delete_register_success(user, firebase):
    register_success_screen.destroy()
    register_screen.destroy()
    ChangeMoviePreference.change_movies_list(user, firebase)


def delete_register_fail():
    register_fail_screen.destroy()


# Designing Main(first) window
def main_account_screen(firebase):
    global main_screen
    global fire_base

    fire_base = firebase
    auth = firebase.auth()
    # choosing a theme
    main_screen = Tk()
    Tk.iconbitmap(main_screen, default="icon (1).ico")
    style = Style(theme='emovie', themes_file='Screens/ttkbootstrap_themes.json')

    # changing the buttons
    style.configure('W.TButton', font=('David', 10))
    style.configure('success.TButton', font=('David', 14))
    style.configure('Login.TButton', font=('David', 14))

    center(main_screen)
    main_screen.geometry("400x200")
    main_screen.title("Account Login")
    Label(text="Welcome", width="300", height="2", font=("David", 16)).pack()
    Label(text="").pack()
    ttk.Button(text="Login", width="30", command=lambda: login(firebase), style='Login.TButton').pack()
    Label(text="").pack()
    ttk.Button(text="Register", width="30", command=lambda: register(auth), style='success.TButton').pack()
    main_screen.mainloop()
