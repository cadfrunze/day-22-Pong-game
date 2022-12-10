from turtle import Turtle
from terenul import Terenul
import random

MOVE_DISTANCE = 4
UNGHI = random.randint(-10, 10)


class Bila(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_cor = self.xcor()
        self.y_cor = self.ycor()

    def miscare_bila(self):
        if int(self.ycor()) > 290:
            pass
        elif int(self.ycor()) < -290:
            pass
        self.goto(x=self.xcor() + UNGHI + 2, y=self.ycor() + UNGHI + 2)
