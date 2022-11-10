from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    with open("password.txt", mode="a") as f:
        f.write(f'\n{web_input.get()} | {email_input.get()} | {password_input.get()}')
    web_input.delete(0, END)
    password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
email_label = Label(text="email:")
email_label.grid(column=0, row=2)
password_label = Label(text="password:")
password_label.grid(column=0, row=3)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()
email_input = Entry(width=35)
email_input.insert(0, "@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)
password_input = Entry()
password_input.grid(column=1, row=3)

password_icon = Button(text="generate password")
password_icon.grid(column=2, row=3)
add_icon = Button(text="Add", width=36, command=add)
add_icon.grid(column=1, row=4, columnspan=2)







window.mainloop()
