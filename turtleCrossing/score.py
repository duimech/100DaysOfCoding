from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(-380, 260)
        self.level = 1
        self.write(f"Level: {self.level}", font=FONT)


    def print_level(self):
        self.write(f"Level: {self.level}", font=FONT)


    def increase_level(self):
        self.clear()
        self.level += 1
        self.print_level()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", font=FONT, align="center")