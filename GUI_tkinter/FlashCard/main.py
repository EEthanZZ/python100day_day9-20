import random
from tkinter import *

import pandas
from pandas import *
BACKGROUND_COLOR = "#B1DDC6"
u = "data/french_words.csv"
a = {}
b = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    o_data = pandas.read_csv(u)
    a = o_data.to_dict(orient="records")
else:
    a = data.to_dict(orient="records")
def next_word():
    global b, flip_timer
    window.after_cancel(flip_timer)
    b = random.choice(a)
    french_words = b["French"]
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=french_words)
    canvas.itemconfig(card_img, image=photo)
    flip_timer = window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=b["English"])
    canvas.itemconfig(card_img, image=back_photo)


def card_known():
    a.remove(b)
    data = pandas.DataFrame(a)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=525, width=800)
photo = PhotoImage(file="images/card_front.png")
back_photo = PhotoImage(file="images/card_back.png")
button_right_img = PhotoImage(file="images/right.png")
button_wrong_img = PhotoImage(file="images/wrong.png")
card_img = canvas.create_image(400, 263, image=photo)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "bold"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

button_wrong = Button(image=button_wrong_img, highlightthickness=0, command=next_word)
button_wrong.grid(column=0, row=1)
button_right = Button(image=button_right_img, highlightthickness=0, command=card_known)
button_right.grid(column=1, row=1)



next_word()



window.mainloop()