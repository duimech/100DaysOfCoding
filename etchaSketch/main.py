# This program is a simulation of the Etch-a-Sketch drawing pad.
# Author: Ray Bolin
# Date: 1/20/2022
# 100DaysOfCoding

from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()


def move_forward():
    my_turtle.forward(10)


def move_backwards():
    my_turtle.backward(10)


def turn_left():
    my_turtle.left(10)


def turn_right():
    my_turtle.right(10)


def clear_screen():
    my_turtle.reset()
    my_turtle.home()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()