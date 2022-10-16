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
from snake import Snake
# move the snake#


# for loop to create the snake body#
screen = Screen()

screen.bgcolor("black")
screen.title("Welcome to the snake game")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.movement()


screen.exitonclick()