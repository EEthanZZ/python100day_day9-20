from turtle import Turtle
from random import randint, choice

START_POSITION_RANGE = randint(-240, 240)
START_POSITION = [(START_POSITION_RANGE, START_POSITION_RANGE),
                  (START_POSITION_RANGE - 20, START_POSITION_RANGE),
                  (START_POSITION_RANGE - 40, START_POSITION_RANGE)]
START_DIRECTION = choice([90, 270])

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body_blocks = []
        self.snake_initial()
        self.head = self.body_blocks[0]

    def snake_initial(self):
        for i in START_POSITION:
            self.new_block(i)
            self.body_blocks[0].setheading(START_DIRECTION)
            # a bug here waiting to be fixed when doing the snake head distance to the wall

    def movement(self):
        for i in range(len(self.body_blocks) - 1, 0, -1):
            new_x = self.body_blocks[i - 1].xcor()
            new_y = self.body_blocks[i - 1].ycor()
            self.body_blocks[i].goto(new_x, new_y)
        self.head.forward(20)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def new_block(self, i):
        snake_body = Turtle('square')
        snake_body.color('white')
        snake_body.penup()
        snake_body.goto(i)
        self.body_blocks.append(snake_body)

    def increase_body(self):
        self.new_block(self.body_blocks[-1].position())

    def reset(self):
        for i in self.body_blocks:
            i.goto(1000, 1000)
        self.body_blocks.clear()
        self.snake_initial()
        self.head = self.body_blocks[0]

