from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

SPEED = 0.1

screen = Screen()

screen.setup(width=800, height= 600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((380,0))
l_paddle = Paddle((-385,0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    
    ball.move()
    
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -285:
        ball.bounce_y() 
    
    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        print(f"xcor {ball.xcor()}")
        print(f"rpaddle {ball.distance(r_paddle)}")
        print(f"lpaddle {ball.distance(l_paddle)}")
        ball.bounce_x()
    
    #detect collision with y axis
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
        
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()
    
screen.exitonclick()