"""
task breakdown

1. create a snake body

2.move the snake

3.control the snake

4. detect collision with food

5. create a scoreboard

6. detect collision with wall

7.detect collision with tail
"""
import time
from turtle import Turtle, Screen
# move the snake#
body_blocks = []

# for loop to create the snake body#
screen = Screen()

screen.bgcolor("black")
screen.title("Welcome to the snake game")
screen.setup(width=600, height=600)
screen.tracer(0)

for i in range(3):
    snake_body = Turtle('square')
    snake_body.color('white')
    snake_body.penup()
    snake_body.goto(40 - i * 20, 0)
    body_blocks.append(snake_body)


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(body_blocks) - 1, 0, -1):
        new_x = body_blocks[i-1].xcor()
        new_y = body_blocks[i-1].ycor()
        body_blocks[i].goto(new_x, new_y)
    body_blocks[0].forward(20)
    body_blocks[0].left(90)


screen.exitonclick()