from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    if len(web_input.get()) < 1 or len(password_input.get()) < 1:
        messagebox.showerror(title="oops", message="do not leave any fileds in empty!")
        web_input.delete(0, END)
        password_input.delete(0, END)
    else:
        is_okay = messagebox.askokcancel(title=web_input.get(), message=f'email:{email_input.get()}\n'
                                                                        f'password:{password_input.get()}')
        if is_okay:
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
