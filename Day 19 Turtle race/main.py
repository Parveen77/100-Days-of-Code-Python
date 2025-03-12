from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def moveForward():
    #tim.setheading(0)
    tim.forward(10)
    
def moveBackward():
    #tim.setheading(180)
    tim.backward(10)
    
def moveClockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    #tim.backward(10)


def moveCounterClockwise():  
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    #tim.forward(10)
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun = moveForward)
screen.onkey(key="s", fun=moveBackward)
screen.onkey(key="d", fun=moveClockwise)
screen.onkey(key="a", fun=moveCounterClockwise)
screen.onkey(key="c", fun=clear)



screen.exitonclick()