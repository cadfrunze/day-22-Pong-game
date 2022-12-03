from turtle import Turtle
from terenul import Terenul
import random

MOVE_DISTANCE = 2
UNGHI = random.randint(1, 359)


class Bila(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.setheading(UNGHI)

    def miscare_bila(self):
        if int(self.ycor()) == 290 or int(self.ycor()) == 291:
            self.setheading(360 - UNGHI)
        elif int(self.ycor()) == -290 or int(self.ycor()) == -291:
            self.setheading(360 + UNGHI)
        self.forward(MOVE_DISTANCE)






