from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.createPaddle(coordinates)

    def createPaddle(self, coordinates):
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(coordinates)
        self.resizemode("user")
        self.shapesize(stretch_len=4)
        self.speed=40

    def up(self):
        if self.ycor()<350:
            self.forward(self.speed)
            
    def down(self):
        if self.ycor()>-350:
            self.forward(-1*self.speed)
    