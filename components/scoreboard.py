from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.lScore=0
        self.rScore=0
        self.hideturtle()
        self.updateScoreboard()
    def updateScoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lScore,align="center", font=("Verdana", 70, "normal"))
        self.goto(100,200)
        self.write(self.rScore,align="center", font=("Verdana", 70, "normal"))

    def lPoint(self):
        self.lScore+=1
        self.updateScoreboard()
        
    def rPoint(self):
        self.rScore+=1
        self.updateScoreboard()