from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-200, y=250)
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.level}", font=FONT, align="left")

    def update(self):
        self.clear()
        self.level += 1
        self.write_score()

    def game_fail(self):
        self.goto(0,0)
        self.write(f"Game Over", font=FONT, align="center")



