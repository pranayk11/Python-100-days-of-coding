import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

# Draw a Square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# Draw a Dashed Line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup() # No drawing when moving
#     timmy.forward(10)
#     timmy.pendown()


# # Drawing different shapes
# colours = ["red", "blue", "green", "yellow", "orange", "wheat", "SeaGreen", "SlateGray"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.left(angle)
#
#
# for shape_side in range(3, 11):
#     timmy.color(random.choice(colours))
#     draw_shape(shape_side)

# # Drawing a random walk
# turtle.colormode(255)
# directions = [0, 90, 180, 270]
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_colour = (r, g, b)
#     return random_colour
#
#
# for _ in range(100):
#     timmy.width(10)
#     timmy.forward(30)
#     timmy.color(random_color())
#     timmy.setheading(random.choice(directions))

# Draw a Spirograph
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.circle(50)
        timmy.color(random_color())
        timmy.left(size_of_gap)


draw_spirograph(10)

screen = Screen()
screen.exitonclick()
