from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SNAKE_SPEED = 0.1

screen = Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(SNAKE_SPEED)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        SNAKE_SPEED *= 0.9

    if snake.head.xcor() > 580 or snake.head.xcor() < -580 or snake.head.ycor() > 580 or snake.head.ycor() < -580:
        scoreboard.reset_scoreboard()
        snake.reset_snake()
        SNAKE_SPEED = 0.1

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()
            SNAKE_SPEED = 0.1


screen.exitonclick()
