# This program is the pong game.
# Author: Ray Bolin
# Date: 1/23/2022
# 100DaysOfCoding

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(position=(350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_running = True
while game_running:
    screen.update()
    time.sleep(ball.move_speed)

    scoreboard.update_score()
    
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50:
        ball.leftright = "left"
        ball.move_speed *= 0.9
        print(ball.move_speed)
    elif ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.leftright = "right"
        ball.move_speed *= 0.9
        print(ball.move_speed)


    if ball.xcor() > 380:
        ball.reset(ball.xcor())
        scoreboard.clear()
        scoreboard.l_score += 1
    elif ball.xcor() < -380:
        ball.reset(ball.xcor())
        scoreboard.clear()
        scoreboard.r_score += 1
    else:
        ball.move()

    
        
        


screen.exitonclick()