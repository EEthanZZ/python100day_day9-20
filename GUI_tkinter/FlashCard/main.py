from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = Canvas()
photo = PhotoImage(file="images/card_front.png")
button_right_img = PhotoImage(file="images/right.png")
button_wrong_img = PhotoImage(file="images/wrong.png")
canvas.create_image(800, 526, image=photo)
canvas.grid(column=0, row=0, columnspan=2)
button_wrong = Button(image=button_wrong_img, highlightcolor=BACKGROUND_COLOR)
button_wrong.grid(column=0, row=1)
button_right = Button(image=button_right_img, highlightcolor=BACKGROUND_COLOR)
button_right.grid(column=1, row=1)


window.mainloop()