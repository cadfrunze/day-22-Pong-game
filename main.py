from turtle import Screen, Turtle
from paletele import Paleta
import random
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1400, height=800)
screen.title(titlestring="Jocul")
screen.listen()

screen.tracer(0)

t2 = Turtle()
t2.penup()
t2.hideturtle()
t2.goto(x=-560, y=-300)
t2.color('white')
t2.pendown()
t2.pensize(5)

for _ in range(4):
    t2.forward(1100)
    t2.left(90)
    t2.forward(600)
    t2.left(90)
t2.goto(x=0, y=-300)
t2.left(90)
t2.color('blue')
t2.penup()
t2.forward(5)
for i in range(30):
    t2.pendown()
    t2.forward(10)
    t2.penup()
    t2.forward(10)

screen.listen()

paleta = Paleta()

time.sleep(0.01)
screen.update()


screen.exitonclick()





