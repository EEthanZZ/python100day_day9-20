from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def change_direction_wall(self):
        self.y_move *= -1

    def change_direction_paddle(self):
        self.x_move *= -1

    def restart_game(self):
        self.goto(0, 0)
        self.change_direction_paddle()
