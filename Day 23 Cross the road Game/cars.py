from turtle import Turtle
import random


CAR_SPEED = 5
MOVE_INCREMENT = 3

COLORS = ["orange", "red", "blue", "pink", "black", "grey"]

class Car_manager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.car_speed = CAR_SPEED
        
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1 :
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            random_y = random.randint(-250,250)
            new_car.goto(360, random_y)
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        