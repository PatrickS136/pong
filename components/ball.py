from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.createBall()

    def createBall(self):
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x=10
        self.y=10
        self.multiplier=1.0

    def move(self):
        self.goto(self.xcor()+(self.x*self.multiplier), self.ycor()+(self.y*self.multiplier))

    def bounceY(self):
        self.y*=-1
        self.multiplier+=0.1

    def bounceX(self):
        self.x*=-1
        self.multiplier+=0.1

    def resetPos(self):
        self.goto(0,0)
        self.bounceX()
        self.multiplier=1.0

    def resetSpeed(self):
        self.multiplier=1.0
        if (self.x<0):
            self.x=-10
        else:
            self.x=10
        if (self.y<0):
            self.y=-10
        else:
            self.y=10
    