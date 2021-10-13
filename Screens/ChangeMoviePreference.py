from ttkbootstrap import Style
from tkinter import ttk

from Screens import MainScreen
from tkinter import *
from MovieRecommendation import MovieSearch
from PyQt5 import QtWidgets
from Screens import LoginRegister


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


#
# def set_movies_list(user, db):
#     global set_movies_menu_screen
#     emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
#     set_movies_menu_screen = Toplevel(LoginRegister.register_screen)
#     center(set_movies_menu_screen)
#     set_movies_menu_screen.title("Set Movies List")
#     # set_movies_menu_screen.geometry("500x500")
#     Label(set_movies_menu_screen, text="Enter New Movies List", font=('Calibri', 16)).pack()
#     # create a dictionary with [emotion:[movie name ]
#     lable_dict = {}
#     for item in emotion_labels:
#         try:
#             movies = db.child(user['localId']).get()
#             name = MovieSearch.search_movie_id(movies.val()[item])
#             lable_dict[item] = [name.title()]
#         except:
#             lable_dict[item] = ["none"]
#
#
#     i = 0
#     for emotion in emotion_labels:
#         label_text = StringVar(set_movies_menu_screen)
#         label_text.set(emotion + " movie:" + lable_dict[emotion][0])
#         print(label_text.get())
#         l = Label(set_movies_menu_screen, textvariable=label_text)
#         l.pack()
#
#         lable_dict[emotion].append(label_text)
#         print(lable_dict[emotion])
#         Button(set_movies_menu_screen, text="change", font=('Calibri', 10), height="1", width="15",
#                command=lambda j=i: change_movie(lable_dict, emotion_labels, j, user, db)).pack(pady=6)
#         i += 1
#
#     Button(set_movies_menu_screen, text="Advance", font=('Calibri', 14), height="2", width="30",
#            command=lambda: saveAndClose()).pack()
#
#     set_movies_menu_screen.mainloop()


# def saveAndClose():
#     set_movies_menu_screen.destroy()
#     LoginRegister.register_sucess()


def movie_list_not_complete_message():
    global movie_list_not_complete
    movie_list_not_complete = Toplevel(change_movies_menu_screen)
    center(movie_list_not_complete)
    movie_list_not_complete.title("Error")
    # login_fail_screen.geometry("400x300")
    Label(movie_list_not_complete, font=("David", 16), text="Please fill the movie list", bg="red").pack()
    Button(movie_list_not_complete, font=("David", 16), text="OK", command=delete_movie_list_message).pack()


def delete_movie_list_message():
    movie_list_not_complete.destroy()




def change_movies_list(user, db):
    # after pressing advance
    def setTheSettingsBeforeDivert(user, db):
        flag = 0
        for value in lable_dict.values():
            if value[0] == 'none':
                flag = 1
                break
        if (flag == 0):
            try:
                change_movies_menu_screen.destroy()
                MainScreen.main_menu.deiconify()
            except:
                LoginRegister.main_screen.deiconify()
        else:
            movie_list_not_complete_message()

    global change_movies_menu_screen
    emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
    lable_dict = {}
    for item in emotion_labels:
        try:
            movies = db.child(user['localId']).get()
            name = MovieSearch.search_movie_id(movies.val()[item])
            lable_dict[item] = [name.title()]
        except:
            lable_dict[item] = ["none"]

    change_movies_menu_screen = Toplevel(LoginRegister.main_screen)

    center(change_movies_menu_screen)



    change_movies_menu_screen.title("Change Movies List")
    Label(change_movies_menu_screen, text="Enter New Movies List", font=('David', 16)).pack()
    i = 0
    for emotion in emotion_labels:
        label_text = StringVar(change_movies_menu_screen)
        label_text.set(emotion + " movie:" + lable_dict[emotion][0])
        l = Label(change_movies_menu_screen, textvariable=label_text)
        l.pack()

        lable_dict[emotion].append(label_text)
        ttk.Button(change_movies_menu_screen, text="change", width="15",
               command=lambda j=i: change_movie(lable_dict, emotion_labels, j, user, db),style='W.TButton').pack(pady=5)
        i += 1

    ttk.Button(change_movies_menu_screen, text="Done" ,width="30",
               command=lambda: setTheSettingsBeforeDivert(user, db),style='success.TButton').pack(pady=6)
    change_movies_menu_screen.geometry("500x500")

    change_movies_menu_screen.mainloop()


def change_movie(lable_dict, emotion_labels, i, user, db):
    # Update the list
    def update(name):
        # Clear the list
        results_list.delete(0, END)
        # Put the results in the list
        res = MovieSearch.search_movie(name)
        if res:
            for key in res.keys():
                key = key.title()
                results_list.insert(END, key)

    # Fill the search bar with the selected box in the list
    def fill_out(e):
        # Deleting whats in the box
        search_box.delete(0, END)
        # Add the chosen one to the search
        search_box.insert(1, results_list.get(ACTIVE))

    # Update Results when key is entered into the search bar
    def check(e):
        update(search_box.get())

    def save_movie(user, db):
        if results_list.get(ACTIVE):
            name = results_list.get(ACTIVE)[:-6]
            movie = MovieSearch.search_movie(name)
            id = movie[results_list.get(ACTIVE).lower()]
            if movie:
                data = {emotion_labels[i]: id}
                db.child(user['localId']).update(data)

                change_movie_screen.destroy()
                # MainScreen.main_menu.deiconify()
                lable_dict[emotion_labels[i]][1].set(emotion_labels[i] + " movie:" + name)
                lable_dict.update({emotion_labels[i]: [name, lable_dict[emotion_labels[i]][1]]})
                change_movies_menu_screen.update_idletasks()

    # def delete_change_movies():
    #     change_movie.destroy()

    global change_movie_screen
    # creating a label
    change_movie_screen = Toplevel(change_movies_menu_screen)
    center(change_movie_screen)

    # change_movie_screen.geometry("500x500")
    my_label = Label(change_movie_screen, text="Enter Movie Name:", font=('David', 14))
    my_label.pack(pady=20)
    # creating entry box
    search_box = Entry(change_movie_screen, font=('David', 12))
    search_box.pack()
    # Creating a results list
    results_list = Listbox(change_movie_screen, width=50)
    results_list.pack(pady=40)
    # adding the default titles
    update("")
    # binding the list on click
    results_list.bind("<<ListboxSelect>>", fill_out)
    # Binding the searchbar
    search_box.bind("<KeyRelease>", check)
    # save button
    Button(change_movie_screen, text="Save", font=('David', 14), height="2", width="30",
           command=lambda: save_movie(user, db)).pack()



