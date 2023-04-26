# import colorgram
# # Extract colors from the image
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import random
import turtle as t
tim = t.Turtle()
t.colormode(255)
color_list = [(202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138),
              (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75),
              (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31),
              (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182),
              (19, 71, 63), (175, 192, 212)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_of_dots = 100
for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
