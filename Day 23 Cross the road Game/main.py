from turtle import Screen
import time
from player import Player
from cars import Car_manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.title("Cross the road ")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")

car_manager = Car_manager()
scoreboard = Scoreboard()


game_on =True

while game_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()
    
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()
            
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_score()



    
screen.exitonclick()