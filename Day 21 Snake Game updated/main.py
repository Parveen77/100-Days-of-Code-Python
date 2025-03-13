from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(SPEED)
    
    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        
    #detect collision with boundary
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        print("Wall collision")
        #game_is_on = False
        #scoreboard.game_over()
        snake.reset()
        scoreboard.reset()
    #detect collision with snake itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 2:
            print(f"Collision with itself {snake.head.distance(segment)}")
            #game_is_on = False
            #scoreboard.game_over()
            snake.reset()
            scoreboard.reset()


screen.exitonclick()