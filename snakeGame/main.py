# This program is the snake game using multiple classes and slicing
# Author: Ray Bolin
# Date: 1/22/2022
# 100DaysOfCoding

from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create a snake body 
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Move the snake 
game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)    

    snake.move_snake()
    # Detect collisions with food and move food
    if snake.head.distance(food) < 18:
        food.refresh()
        scoreboard.update_score()
        snake.extend_snake()

    # Detect collisions with wall
    if snake.head.xcor() < -285 or snake.head.xcor() > 285 or snake.head.ycor() < -285 or snake.head.ycor() > 285:
        game_is_running = False
        scoreboard.game_over()

    # Detect collisions with tail
    for segment in snake.segment_list[1:]:
        if snake.head.distance(segment) < 10:
            game_is_running = False
            scoreboard.game_over()



    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


screen.exitonclick()