from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color:")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "Purple"]

y_axis = -100
all_turtles = []

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-240, y=y_axis)
    y_axis += 40
    all_turtles.append(tim)
    

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            Winning_color = turtle.pencolor()
            if Winning_color == user_bet:
                print(f"You've won. The {Winning_color} turtle is the winner")
            else:
                print(f"You've lost. The {Winning_color} turtle is the winner")
                
            is_race_on = False
            
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        
            
 
screen.exitonclick()