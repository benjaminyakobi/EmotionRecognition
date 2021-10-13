from tkinter import *
from tkinter import ttk

from EmotionRecognition import EmotionRecognition
from MovieRecommendation.GetRecommendation import get_recommendations
from Screens import MainScreen


# open the camera and get the emotions
def open_camera(user, db):
    MainScreen.main_menu.withdraw()
    result = EmotionRecognition.start()
    if len(result) > 0:
        emotion_recognition_results_page(result, user, db)
    else:
        no_face_detected_screen()


# get the recommendation for the detected emotion
def emotion_recognition_results_page(result, user, db):
    restr = ""
    res = {}
    res["len"] = len(result)
    # counting each emotion
    for e in result:
        if e not in res.keys():
            res[e] = 1
        else:
            res[e] = res[e] + 1

    res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))

    for e in res.keys():
        if e != "len":
            restr += e + ": {0:.2f}%\n".format((int(res[e]) / int(res["len"])) * 100)

    # creating the screen
    global results_screen
    results_screen = Toplevel(MainScreen.main_menu)
    results_screen.title("Emotions Recognition Page")
    # results_screen.geometry("400x300")
    Label(results_screen, text="Emotions Detected:", font=("David 16 underline")).pack()
    Label(results_screen, text=restr, font=("David", 14)).pack()
    Label(results_screen, text="Recommended For You:", font=("David 16 underline")).pack()

    # listbox = Listbox(results_screen)
    # listbox.pack(pady=10)
    # getting the movie from firebase
    movies = db.child(user['localId']).get()
    selected = movies.val()
    # getting recommendation
    results = get_recommendations(selected[list(res.keys())[1]])
    # adding the results into the page
    res = ""
    print(results)
    print(results.values)
    i = 1
    for key in results.values:
        # key = key.title()
        print(key.title())
        res += str(i) + ". " + key.title() + "\n"
        i += 1
        # listbox.insert(END, key)
    print(res)
    Label(results_screen, text=res, font=("David, 14")).pack()
    ttk.Button(results_screen, text="Back to Main Menu", style='success.TButton', command=back_to_main).pack()


# in case there is no emotion detected
def no_face_detected_screen():
    global no_results_screen
    no_results_screen = Toplevel(MainScreen.main_menu)
    Label(no_results_screen, text="No emotions been detected please try again", font=("David 16")).pack()
    ttk.Button(no_results_screen, text="Back to Main Menu", style='success.TButton', command=back_to_main).pack()


def back_to_main():
    try:
        results_screen.destroy()
    except:
        no_results_screen.destroy()

    MainScreen.main_menu.deiconify()
