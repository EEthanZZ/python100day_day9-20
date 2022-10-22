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
PADDLE_LOCATION = [(350,)]

# create the screen

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
screen = Screen()
screen.bgcolor("black")
screen.title("Welcome to the Pong game")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# create the paddle
ball = Ball()
ga_is_on = True
while ga_is_on:
    screen.update()
    ball.ball_move()

screen.exitonclick()
