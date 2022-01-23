# This program spawns 6 turtles that race each other.
# Author: Ray Bolin
# Date: 1/8/2022
# 100DaysOfCoding

from turtle import Turtle, Screen
import random

turtle_red = Turtle()
turtle_red.color("red")

turtle_blue = Turtle()
turtle_blue.color("blue")

turtle_green = Turtle()
turtle_green.color("green")

turtle_grey = Turtle()
turtle_grey.color("grey")

turtle_purple = Turtle()
turtle_purple.color("purple")

turtle_orange = Turtle()
turtle_orange.color("orange")

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()

pos = -125
for turtle in screen.turtles():
    turtle.shape("turtle")
    turtle.turtlesize(2,2)
    turtle.penup()   
    turtle.setpos(-275,pos)
    pos += 50

user_guess = str.lower(screen.textinput("Predict the winner", "Which turtle will win the race?"))
winner = ""
while winner == "":
    for turtle in screen.turtles():
        turtle.forward(random.randint(1,5))
        
        if turtle.xcor() >= 275:
            winner = turtle.pencolor()


if user_guess == winner:
    print(f"You are correct! {winner} won!")
else:
    print(f"You are incorrect. The winner was {winner}.")

