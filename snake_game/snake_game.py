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
from food import Food
from score_board import Score_board
# move the snake#


# for loop to create the snake body#
screen = Screen()

screen.bgcolor("black")
screen.title("Welcome to the snake game")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
score = Score_board()

screen.onkey(snake.snake_up, "w")
screen.onkey(snake.snake_down, "s")
screen.onkey(snake.snake_left, "a")
screen.onkey(snake.snake_right, "d")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.movement()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
    # 6. detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False


screen.exitonclick()