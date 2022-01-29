from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto_start()

    def move_up(self):
        self.forward(10)

    def goto_start(self):
        self.setposition(0, -280)