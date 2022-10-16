from turtle import Turtle


class Snake:
    def __init__(self):
        self.body_blocks = []
        self.snake_initial()

    def snake_initial(self):
        for i in range(3):
            snake_body = Turtle('square')
            snake_body.color('white')
            snake_body.penup()
            snake_body.goto(40 - i * 20, 0)
            self.body_blocks.append(snake_body)
