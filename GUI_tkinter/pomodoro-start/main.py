import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_time():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(fg=GREEN)
    else:
        count_down(short_break_sec)
        timer_label.config(fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif int(count_sec) < 10:
        count_sec = "0" + str(count_sec)
    if int(count_min) < 10:
        count_min = f'0{count_min}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    if count == 0:
        start_time()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightbackground=YELLOW)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_time)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN)
timer_label.config(bg=YELLOW)
timer_label.grid(column=1, row=0)
check_label = Label(text="✔︎", bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()
