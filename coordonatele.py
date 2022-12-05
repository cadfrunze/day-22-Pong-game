from turtle import Turtle
from bila import Bila


class Coordonate(Turtle):
    def __int__(self):
        super().__init__()
        # self.penup()
        self.color('white')
        # self.hideturtle()
        # self.x_cor = Bila.xcor
        # self.y_cor = Bila.ycor

    def afisare_coordonate(self):
        self.goto(x=-200, y=200)
        self.write(arg=f"blaththghghfg", move=False, align='center')
