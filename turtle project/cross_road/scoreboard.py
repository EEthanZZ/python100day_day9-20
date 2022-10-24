from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-200, y=250)
        self.write(f"Level: {self.level}", font=FONT, align="left")

    def update(self):
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT, align="left")




