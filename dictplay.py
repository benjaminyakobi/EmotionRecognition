
dict = {'Angry': ['Avengers: Age Of Ultron', '<tkinter.StringVar object at 0x0000018B3B213580>'], 'Disgust': ['none', '<tkinter.StringVar object at 0x0000018B3B2130A0>'], 'Fear': ['Dancer, Texas Pop. 81',' <tkinter.StringVar object at 0x0000018B3C09E490>'], 'Happy': ['Harry Potter And The Half-Blood Prince', '<tkinter.StringVar object at 0x0000018B3C09E370>'], 'Neutral': ['Harry Potter And The Half-Blood Prince', '<tkinter.StringVar object at 0x0000018B3C09E2E0>'], 'Sad': ['Blazing Saddles', '<tkinter.StringVar object at 0x0000018B3C09EF10>'], 'Surprise': ['Deadpool', '<tkinter.StringVar object at 0x0000018B3D7470A0>']}
print(dict)
for value in dict.values():
    print (value)
    if value[0]=='none':
        print('none is foud')
        break
