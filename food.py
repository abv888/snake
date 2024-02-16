from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-540, 540), y=random.randint(-540, 540))
