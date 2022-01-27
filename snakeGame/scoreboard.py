from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()

        with open("highscore.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.score = 0
        # self.high_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} - HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        
        with open("highscore.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()