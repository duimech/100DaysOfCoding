from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.updown = "up"
        self.leftright = "right"
        self.move_speed = 0.1
        
    def move(self):
        if self.ycor() >= 280:
            self.updown = "down"
        elif self.ycor() <= -280:
            self.updown = "up"

        if self.leftright == "right":
            x_cor = self.xcor() + 10
        elif self.leftright == "left":
            x_cor = self.xcor() - 10

        if self.updown == "up":
            y_cor = self.ycor() + 10
            self.goto(x_cor, y_cor)
        elif self.updown == "down":
            y_cor = self.ycor() - 10

        self.goto(x_cor, y_cor)


    def reset(self, xcor):
        if xcor > 380:
            self.goto(0,0)
            self.leftright = "left"
        elif xcor < -380:
            self.goto(0,0)
            self.leftright = "right"
        
        self.move_speed = 0.1
            




