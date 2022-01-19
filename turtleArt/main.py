# This program uses the Python turtle to randomly move around and change the color line it draws
# Author: Ray Bolin
# Date: 1/18/2022
# 100DaysOfCoding


from turtle import Turtle, Screen
import random 

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.speed(0)
my_turtle.pensize(20)

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

def random_color():
    colors = ["red", "blue", "green", "maroon", "cyan", "aqua", "gold", "brown"]
    return random.choice(colors)

def random_move(self):
    num = random.randint(0,1)
    if num == 0:
        self.right(90)
        self.forward(50)
    else:
        self.left(90)
        self.forward(50)


my_turtle.speed(0)
my_turtle.pensize(10)

i=0
while i < 100:
    my_turtle.color(random_color())
    random_move(my_turtle)
    i += 1

screen = Screen()
screen.exitonclick()
