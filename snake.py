from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        number_of_segments = 3
        for i in range(number_of_segments):
            position = (-20 * i, 0)
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for snake_segment_index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[snake_segment_index - 1].xcor()
            y = self.segments[snake_segment_index - 1].ycor()
            self.segments[snake_segment_index].goto(x, y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
