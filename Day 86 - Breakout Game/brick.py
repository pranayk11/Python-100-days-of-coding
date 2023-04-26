from turtle import Turtle
import random


class Brick(Turtle):
    colors = ['green', 'red', 'brown', 'orange', 'blue', 'yellow', 'purple']

    def __init__(self, position):
        super().__init__()
        self.color(random.choice(self.colors))
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=0.75)
        self.penup()
        self.goto(position)