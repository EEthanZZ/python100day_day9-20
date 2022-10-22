from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(location)

    def create_paddle(self):
        self.goto()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)


