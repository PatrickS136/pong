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
myScoreboard=Scoreboard(150,280)

# Game logic
gameOn=True
yBound=screenHeight/2-30
xBound=screenWidth/2-20
paddleBound=70
while gameOn:
    sleep(0.05)
    myScreen.update()
    myBall.move()
    if myBall.ycor()>yBound or myBall.ycor()<-1*yBound:
        myBall.bounceY()
    if (myBall.distance(rightPaddle)<paddleBound and myBall.xcor()>xBound-60 and myBall.xcor()<xBound-30) or (myBall.distance(leftPaddle)<paddleBound and myBall.xcor()<-(xBound-60) and myBall.xcor()>-(xBound-30)):
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