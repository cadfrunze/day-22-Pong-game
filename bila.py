from turtle import Turtle
from terenul import Terenul
import random


class Bila(Turtle):
    """Bila"""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        lista = [-5, 5]
        self.alege = random.choice(lista)
        self.viteza = self.alege
        self.x_move = self.viteza
        self.y_move = self.viteza

    def miscare_bila(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def sari_inapoi(self):
        self.y_move = self.y_move * -1

    def sari_inapoi_paleta(self):
        self.x_move = self.x_move * -1

    def reseteaza(self):
        self.clear()
        self.home()
        self.sari_inapoi_paleta()
        self.miscare_bila()
