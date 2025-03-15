from turtle import Turtle

FONT_STYLE = ( "courier", 25, "normal" )

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-50, 260)
        self.write(self.l_score, align="center", font=FONT_STYLE)
        self.goto(50, 260)
        self.write(self.r_score, align="center", font=FONT_STYLE)
    
    def l_point(self):
        self.l_score += 1
        self.update_score()
        
    
    def r_point(self):
        self.r_score += 1
        self.update_score()