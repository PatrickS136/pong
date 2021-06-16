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
myScreen.setup(width=800, height=600)
myScreen.title("Pong")

# Ball
myBall=Ball()

# Paddle
rightPaddle=Paddle((350,0))
leftPaddle=Paddle((-350,0))

# Key presses
myScreen.onkeypress(rightPaddle.up,"Up")
myScreen.onkeypress(rightPaddle.down,"Down")
myScreen.onkeypress(leftPaddle.up,"w")
myScreen.onkeypress(leftPaddle.down,"s")

# Scoreboard
myScoreboard=Scoreboard()

# Game logic
gameOn=True
while gameOn:
    sleep(0.05)
    myScreen.update()
    myBall.move()
    if myBall.ycor()>280 or myBall.ycor()<-280:
        myBall.bounceY()
    if (myBall.distance(rightPaddle)<50 and myBall.xcor()>320 and myBall.xcor()<350) or (myBall.distance(leftPaddle)<50 and myBall.xcor()<-320 and myBall.xcor()>-350):
        myBall.bounceX()
    if (myBall.xcor()>380):
        myBall.resetPos()
        myScoreboard.lPoint()
        myBall.resetSpeed()
    if (myBall.xcor()<-380):
        myBall.resetPos()
        myScoreboard.rPoint()
        myBall.resetSpeed()

# Exit on click
myScreen.exitonclick()