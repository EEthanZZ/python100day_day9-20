from turtle import Turtle
from random import randint, choice

START_POSITION_RANGE = randint(-240, 240)
START_POSITION = [(START_POSITION_RANGE, START_POSITION_RANGE),
                  (START_POSITION_RANGE-20, START_POSITION_RANGE),
                  (START_POSITION_RANGE-40, START_POSITION_RANGE)]
START_DIRECTION = choice([90, 270])

class Snake:
    def __init__(self):
        self.body_blocks = []
        self.snake_initial()

    def snake_initial(self):
        for i in START_POSITION:
            snake_body = Turtle('square')
            snake_body.color('white')
            snake_body.penup()
            snake_body.goto(i)
            self.body_blocks.append(snake_body)

    def movement(self):
        for i in range(len(self.body_blocks) - 1, 0, -1):
            new_x = self.body_blocks[i - 1].xcor()
            new_y = self.body_blocks[i - 1].ycor()
            self.body_blocks[i].goto(new_x, new_y)
        self.body_blocks[0].left(START_DIRECTION)
        self.body_blocks[0].forward(20)