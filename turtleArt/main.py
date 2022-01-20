# This program uses the Python turtle to randomly move around and change the color line it draws
# Author: Ray Bolin
# Date: 1/18/2022
# 100DaysOfCoding


# from turtle import Turtle
import turtle as t
import random 

my_turtle = t.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(0)
my_turtle.pensize(1)

# color mode is from the class turtle, not our object
t.colormode(255)

# for _ in range(15):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()

# def random_color():
#     colors = ["red", "blue", "green", "maroon", "cyan", "aqua", "gold", "brown"]
#     return random.choice(colors)

# def draw_shape(num_of_sides):

#     my_turtle.pencolor(random_color())
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):        
#         my_turtle.forward(100)
#         my_turtle.right(angle)


# for num_of_sides in range(3,11):
#     draw_shape(num_of_sides)
#     num_of_sides += 1

# def random_color():
#     colors = ["red", "blue", "green", "maroon", "cyan", "aqua", "gold", "brown"]
#     return random.choice(colors)

def random_rgb():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

# def random_move(self):
#     num = random.randint(0,1)
#     if num == 0:
#         self.right(90)
#         self.forward(50)
#     else:
#         self.left(90)
#         self.forward(50)

def draw(gap_size):
    for _ in range(int(360 / gap_size)):
        my_turtle.color(random_rgb())
        # random_move(my_turtle)
        my_turtle.circle(100)
        my_turtle.left(gap_size)
    

draw(4)

screen = t.Screen()
screen.exitonclick()
