from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)
        self.q_next = self.canvas.create_text(150, 125, width=250, text="word", font=FONT, fill=THEME_COLOR)

        self.right_photo = PhotoImage(file="images/true.png")
        self.wrong_photo = PhotoImage(file="images/false.png")

        self.button_right = Button(image=self.right_photo, highlightthickness=0, command=self.correct)
        self.button_right.grid(column=0, row=2, padx=20, pady=20)
        self.button_wrong = Button(image=self.wrong_photo, highlightthickness=0, command=self.wrong)
        self.button_wrong.grid(column=1, row=2, padx=20, pady=20)

        self.score_text = Label(text=f"Score:", bg=THEME_COLOR, font=FONT, fg="white")
        self.score_text.grid(row=0, column=1, padx=20, pady=20)

        self.window.title("Quiz")

        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self)
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.q_next, text=q_text)

    def correct(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_q)

