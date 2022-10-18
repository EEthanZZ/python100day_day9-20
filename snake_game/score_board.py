from turtle import Turtle


class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=240)
        self.color("white")
        self.score = 0
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", font=("Arial", 24, "normal"), align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(f"game over", font=("Arial", 24, "normal"), align="center")