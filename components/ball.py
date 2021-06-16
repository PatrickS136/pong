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

    def move(self):
        self.goto(self.xcor()+self.x, self.ycor()+self.y)

    def bounceY(self):
        self.y*=-1

    def bounceX(self):
        self.x*=-1

    def resetPos(self):
        self.goto(0,0)
        self.bounceX()

    def resetSpeed(self):
        if (self.x<0):
            self.x=-10
        else:
            self.x=10
        if (self.y<0):
            self.y=-10
        else:
            self.y=10
    