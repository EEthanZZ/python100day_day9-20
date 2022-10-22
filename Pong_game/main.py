"""
create the screen

Create and move a paddle

Create the second paddle

create the ball and make it move

detect collision with wall and bounce

detect with paddle

detect when paddle misses

keep score
"""

# create the screen
from turtle import Turtle, Screen
tim = Turtle()


screen = Screen()
screen.bgcolor("black")
screen.title("Welcome to the Pong game")
screen.setup(width=800, height=600)
screen.exitonclick()


