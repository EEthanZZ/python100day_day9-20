import random
from tkinter import *

import pandas
from pandas import *
BACKGROUND_COLOR = "#B1DDC6"


data = pandas.read_csv("data/french_words.csv")
a = data.to_dict(orient="records")
print(a)
def next_word():
    b = random.choice(a)
    french_words = b["French"]
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=french_words)

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = Canvas(height=525, width=800)
photo = PhotoImage(file="images/card_front.png")
button_right_img = PhotoImage(file="images/right.png")
button_wrong_img = PhotoImage(file="images/wrong.png")
canvas.create_image(400, 263, image=photo)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "bold"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

button_wrong = Button(image=button_wrong_img, highlightthickness=0, command=next_word)
button_wrong.grid(column=0, row=1)
button_right = Button(image=button_right_img, highlightthickness=0, command=next_word)
button_right.grid(column=1, row=1)


next_word()

window.mainloop()