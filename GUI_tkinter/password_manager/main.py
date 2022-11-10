from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:", width=20)
web_label.grid(column=0, row=1)
email_label = Label(text="email:", width=20)
email_label.grid(column=0, row=2)
password_label = Label(text="password:", width=15)
password_label.grid(column=0, row=3)

password_icon = Button(text="generate password")
password_icon.grid(column=2, row=3)
add_icon = Button(text="Add", width=25)
add_icon.grid(column=1, row=4)






window.mainloop()
