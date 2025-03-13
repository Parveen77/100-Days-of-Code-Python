from turtle import Turtle



FONT_STYLE = ( "courier", 15, "normal" )
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.score = 0
        
        with open("data.txt") as file:
            self.high_score = int(file.read())

        #self.high_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , align="center", font=FONT_STYLE)
          
      
    def increase_score(self):
        
        self.score +=1  
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT_STYLE)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score =self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
