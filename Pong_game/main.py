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
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard
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
score = ScoreBoard()
ga_is_on = True
while ga_is_on:
    screen.update()
    time.sleep(0.1)
    ball.ball_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_direction_wall()

    # detect collision with right paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.change_direction_paddle()

    if ball.xcor() > 380:
        ball.restart_game()
        score.l_point()

    if ball.xcor() < -380:
        ball.restart_game()
        score.r_point()
screen.exitonclick()
