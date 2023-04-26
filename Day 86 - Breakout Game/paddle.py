from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 15
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 15
        self.goto(new_x, self.ycor())
