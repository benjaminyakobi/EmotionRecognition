from tkinter import *
from tkinter import ttk, messagebox

from ttkbootstrap import Style

from Screens import ChangeMoviePreference
from Screens import LoginRegister
from Screens import EmotionRecognitionScreen
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
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2
    toplevel.geometry("+%d+%d" % (x, y))


def goto_change_movies_list(user, db):
    main_menu.withdraw()
    ChangeMoviePreference.change_movies_list(user,db)
    LoginRegister.main_screen.deiconify()

def checklist(user, db):
    try:
        movies = db.child(user['localId']).get()
        name = movies.val()
        if len(name) ==7:
            EmotionRecognitionScreen.open_camera(user, db)
        else:
            messagebox.showerror(title="Error", message="You need to fill your movie list before recommendation")

    except:
        messagebox.showerror(title="Error", message="You need to fill your movie list before recommendation")


def mainMenu(user, firebase):
    def signout():
        auth = firebase.auth()
        auth
        main_menu.destroy()


    global main_menu
    main_menu = Toplevel(LoginRegister.main_screen)


    db = firebase.database()
    center(main_menu)
    main_menu.title("Hello There")

    # main_menu.geometry("600x500")
    # Label(recommendations_screen, text="Recommended For You:").pack()
    ttk.Button(main_menu, text="Open Camera For Emotions Recognition",  width="45",
           command=lambda: checklist(user, db)).pack()
    ttk.Button(main_menu, text="Change Your Movies List",  width="45",
           command=lambda: goto_change_movies_list(user, db)).pack()

    main_menu.mainloop()


