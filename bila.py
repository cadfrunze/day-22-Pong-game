from turtle import Turtle
from terenul import Terenul
import random

lista = [-5, 5]
UNGHI = random.choice(lista)


class Bila(Turtle):
    """Bila"""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = UNGHI
        self.y_move = UNGHI

    def miscare_bila(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def sari_inapoi(self):
        self.y_move = self.y_move * -1

    def sari_inapoi_paleta(self):
        self.x_move = self.x_move * -1

