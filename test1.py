from turtle import Screen, Turtle
import random
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1200, height=800)
screen.listen()
screen.tracer(0)
t2 = Turtle()
t2.penup()
t2.hideturtle()
t2.goto(x=-580, y=-300)
t2.color('white')
t2.pendown()
t2.pensize(5)
t2.forward(1160)
t2.setheading(90)
t2.forward(600)
t2.setheading(180)
t2.forward(1160)
t2.setheading(270)
t2.forward(600)
t1 = Turtle('circle')
t1.color('blue')
# t1.penup()
unghi = random.randint(40, 359)
while unghi == 90 or unghi == 180:
    unghi = random.randint(10, 359)
print(unghi)
t1.setheading(unghi)
MOVE_DISTANCE = 15
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0
# lungimea = 580
# latimea = 300

joc = True
while joc:
    time.sleep(0.1)
    screen.update()
    t1.penup()
    t1.forward(MOVE_DISTANCE)
    # pt ycor()
    if t1.xcor() >= 560 or t1.xcor() <= -560:
        unghi = 180 - unghi
        t1.setheading(unghi)
    elif t1.ycor() >= 285 or t1.ycor() <= -285:
        unghi = 360 - unghi
        t1.setheading(unghi)










screen.exitonclick()