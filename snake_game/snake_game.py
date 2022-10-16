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
from turtle import Turtle, Screen

#for loop to create the snake body#
for i in range(3):
    snake_body = Turtle('square')
    snake_body.color('white')
    snake_body.goto(40-i*20, 0)




screen = Screen()
screen.bgcolor("black")
screen.title("Welcome to the snake game")
screen.setup(width=600, height=600)
screen.exitonclick()
