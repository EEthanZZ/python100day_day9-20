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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightbackground=YELLOW)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightbackground=YELLOW)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"),fg=GREEN)
timer_label.config(bg=YELLOW)
timer_label.grid(column=1, row=0)
check_label = Label(text="✔︎", bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()