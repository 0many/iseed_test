## 3
# from tkinter import *
# window = Tk()
# def rdo_change():
#   if var.get() == 1:
#         label1.configure(text = "벤츠")
#   else:
#         label1.configure(text = "포르쉐")
#
# var = IntVar(value = 1)
# rdo1 = Radiobutton(window, text = "벤츠", variable = var, value = 1)
# rdo2 = Radiobutton(window, text = "포르쉐", variable = var, value = 2)
# label1 = Label(window, text="선택한 차량", fg="red")
#
# rdo1.pack()
# rdo2.pack()
# label1.pack()
#
# window.mainloop()

## 4
# from tkinter import *
# window=Tk()
#
# button1 = Button(window, text = "버튼1")
# button2 = Button(window, text = "버튼2")
# button3 = Button(window, text = "버튼3")
#
# button1.pack(side=BOTTOM)
# button2.pack(side=BOTTOM)
# button3.pack(side=BOTTOM)
# window.mainloop()

# (1) LEFT
# (2) RIGHT
# (3) TOP
# (4) BOTTOM

## 5
# from tkinter import *
# from time import *
#
# fnameList = ["jejul.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
# num = 0
#
# def clickNext():
#     global num
#     num += 1
#     if num > len(fnameList):
#         num = 0
#     pLabel.configure(text=fnameList[num])
#
# def clickPrev() :
#     global num
#     num -= 1
#     if num < 0:
#         num = len(fnameList) - 1
#     pLabel.configure(text=fnameList[num])
#
# window = Tk()
# window.geometry("650x200")
#
# pLabel = Label(window, text=fnameList[num])
# pLabel.pack()
#
# nextButton = Button(window, text="다음>>", command=clickNext)
# nextButton.place(x=400, y=10)
#
# prevButton = Button(window, text="<<이전", command=clickPrev)
# prevButton.place(x=200, y=10)
#
# window.mainloop()

## Self Study 10-2
from tkinter import *
import random

btnList = [None] * 9
fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif",
             "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif", "pie-gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

window = Tk()
window.geometry("210x210")

def shuffle_images():
    random.shuffle(btnList)
    for i, button in enumerate(btnList):
        button.grid(row=i//3, column=i%3)

for i in range(0, 9):
    photoList[i] = PhotoImage(file="gif/" + fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].grid(row=i, column=k)
        num += 1

shuffle_button = Button(window, text="Shuffle", command=shuffle_images)
shuffle_button.grid(row=3, column=0, columnspan=3)

window.mainloop()

