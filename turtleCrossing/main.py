# This program is a game to get a turtle across a street without being hit by a car.
# Author: Ray Bolin
# Date: 1/26/2022
# 100DaysOfCoding

from turtle import Screen
from player import Player
from car import Car
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

car = Car()
player = Player()
score = Score()

screen.onkey(player.move_up, "Up")

game_running = True
while game_running == True:
    car.create_car()
    score.print_level()
    screen.update()
    # Make the cars go faster as the level increases
    time.sleep(0.1)
    
    # Player makes it across without getting hit
    if player.ycor() > 280:
        score.increase_level()
        car.increase_speed()
        player.goto_start()
        

    # Check to see if player gets hit
    for cars in car.car_list:
        if cars.distance(player) < 20:
            score.game_over()
            game_running = False

    # Move all of the cars
    car.move()

screen.exitonclick()