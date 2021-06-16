# Imports
from turtle import Screen, Turtle
from time import sleep
from components.paddle import Paddle
from components.ball import Ball
from components.scoreboard import Scoreboard

# Screen setup
myScreen=Screen()
myScreen.bgcolor("black")
myScreen.listen()
myScreen.tracer(0)
screenWidth=1400
screenHeight=800
myScreen.setup(width=screenWidth, height=screenHeight)
myScreen.title("Pong")

# Ball
myBall=Ball()

# Paddle
rightPaddle=Paddle((screenWidth/2-50,0))
leftPaddle=Paddle((-(screenWidth/2-50),0))

# Key presses
myScreen.onkeypress(rightPaddle.up,"Up")
myScreen.onkeypress(rightPaddle.down,"Down")
myScreen.onkeypress(leftPaddle.up,"w")
myScreen.onkeypress(leftPaddle.down,"s")

# Scoreboard
myScoreboard=Scoreboard()

# Game logic
gameOn=True
yBound=370
xBound=680
paddleBound=70
while gameOn:
    sleep(0.05)
    myScreen.update()
    myBall.move()
    if myBall.ycor()>yBound or myBall.ycor()<-1*yBound:
        myBall.bounceY()
    if (myBall.distance(rightPaddle)<paddleBound and myBall.xcor()>620 and myBall.xcor()<650) or (myBall.distance(leftPaddle)<paddleBound and myBall.xcor()<-620 and myBall.xcor()>-650):
        myBall.bounceX()
    if (myBall.xcor()>xBound):
        myBall.resetPos()
        myScoreboard.lPoint()
        myBall.resetSpeed()
    if (myBall.xcor()<-1*xBound):
        myBall.resetPos()
        myScoreboard.rPoint()
        myBall.resetSpeed()

# Exit on click
myScreen.exitonclick()