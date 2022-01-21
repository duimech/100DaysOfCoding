# This program draws a 10x10 grid of dots with differnt colors that are equally spaced. 
# Author: Ray Bolin
# Date: 1/19/2022
# 100DaysOfCoding

# Used colorgram to pull colors from an image and made a list of tuples to use in the program.
# import colorgram

# colors = colorgram.extract('/home/duimech/Python/100DaysOfCoding/spotPainting/hirst.jpg', 15)
# rgb_tuple = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tup = (r, g, b)
#     rgb_tuple.append(tup)

# print(rgb_tuple)

# Program requirements:
# 10 rows and 10 columns of spots
# spots are 20 in size
# 50 paces apart

import turtle as t
import random

# List of tuples for our painting
color_list = [(188, 74, 20), (56, 34, 13), (149, 26, 9), (237, 226, 77), (24, 31, 60), (113, 167, 210), (45, 85, 143), (217, 154, 82), (34, 50, 124), (191, 144, 25), (26, 51, 29), (201, 93, 126)]

t.colormode(255)
my_turtle = t.Turtle()
my_turtle.penup()

for y in range(-250,250,50):
    my_turtle.setpos(-250,y)

    for x in range(10):
        my_turtle.color(random.choice(color_list))
        my_turtle.pendown()
        my_turtle.dot(20)
        my_turtle.penup()
        my_turtle.forward(50)

my_turtle.hideturtle()
screen = t.Screen()
screen.exitonclick()