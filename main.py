from turtle import Screen, Turtle
from paletele import Paleta
from terenul import Terenul
import random
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1400, height=800)
screen.title(titlestring="Jocul")
screen.listen()

screen.tracer(0)
screen.listen()
terenul = Terenul()
paleta = Paleta()

time.sleep(0.01)
screen.update()


screen.exitonclick()





