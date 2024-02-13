from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor("black")
screen.title("Snake")

for i in range(3):
    segment = Turtle("square")
    segment.color("white")
    segment.goto(x=-20 * i, y=0)

screen.exitonclick()