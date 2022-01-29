from turtle import Turtle
import random

class Car:
    def __init__(self):
        self.car_list = []
        self.move_speed = 10

    
    def create_car(self):
        num = random.randint(1,6)
        if num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.resizemode("user")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            colors = ["orange", "red", "yellow", "green", "blue", "purple", "black"]
            new_car.color(random.choice(colors))
            rand_y = random.randint(-250,250)
            new_car.setposition(360, rand_y)
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.backward(self.move_speed)

    def increase_speed(self):
        self.move_speed += 2