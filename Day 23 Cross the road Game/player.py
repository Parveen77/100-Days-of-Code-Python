from turtle import Turtle

FONT_STYLE = ( "courier", 25, "normal" )
MOVE_DISTANCE = 10

POSITION = (0, -280)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.goto(POSITION)
        self.setheading(90)
        
    def go_up(self):
        self.forward(MOVE_DISTANCE)
        
    def goto_start(self):
        self.goto(POSITION)
    
    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False