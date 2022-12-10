from turtle import Turtle


class Coordonate(Turtle):
    def __int__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=0)
        self.color('white')
        self.hideturtle()


