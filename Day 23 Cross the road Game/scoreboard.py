from turtle import Turtle

FONT_STYLE = ( "courier", 20, "normal" )

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-380, 270)
        self.write(f"LEVEL:{self.score}", align="left", font=FONT_STYLE)
    
    
    def increase_score(self):
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.goto(-50,0)
        self.write(f"GAME OVER", align="left", font=FONT_STYLE)
        