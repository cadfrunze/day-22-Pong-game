from turtle import Turtle
from terenul import Terenul
import random

MOVE_DISTANCE = 1
UNGHI = random.randint(1, 359)


class Bila(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.speed('slow')
        self.setheading(UNGHI)
        self.joc_bila = True
        # self.miscare_bila()
        self.verificare()

    def miscare_bila(self):
        self.forward(MOVE_DISTANCE)

    def verificare(self):
        if int(self.ycor()) >= 290:
            self.setheading(360 - UNGHI)
        elif int(self.ycor()) <= -290:
            self.setheading(360 + UNGHI)
        self.miscare_bila()






