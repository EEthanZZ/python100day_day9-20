from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=400, height=200)
window.config(pady=50, padx=50)
text_input = Entry(width=10)
text_input.grid(column=1, row=0)


def cal():
    result = float(text_input.get()) * 1.609
    label4.config(text=result)


label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)
label3 = Label(text="KM")
label3.grid(column=2, row=1)
label4 = Label(text=0)
label4.grid(column=1, row=1)

button = Button(text="Calculate", command=cal)
button.grid(column=1, row=2)

window.mainloop()