import turtle as t
import random


tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

direction = [0,90,180,270]
tim.speed("fastest")


def shapes(sides):
    tim.penup()
    tim.sety(-100)
    tim.pendown()
    tim.color(random_color())
    heading = int(360/sides)
    for _ in range(sides):
        
        tim.forward(100)
        tim.setheading(tim.heading() + heading)     #(tim.heading() - heading) will prdouce shapes in downward diretion 

def many_shapes(number_of_shapes):        
    for side in range(3,number_of_shapes):
        shapes(side)

#many_shapes(10)

def random_walk(steps):
    tim.pensize(15)
    for _ in range(steps):
        tim.color(random_color())
        tim.setheading(random.choice(direction))
        tim.forward(30)


def spirograph(gap):
    heading = tim.heading()
    
    for _ in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+gap)
        
spirograph(5)

screen = t.Screen()
screen.exitonclick()
