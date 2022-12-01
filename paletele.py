from turtle import Turtle

YPOS = 20


class Paleta(Turtle):
    """Creearea paletei"""

    def __init__(self, position, culoarea):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color(culoarea)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.position_obj = position
        self.pozitia(position_obj=self.position_obj)

    def pozitia(self, position_obj):
        self.goto(x=position_obj[0], y=position_obj[1])

    def move_nord(self):
        self.goto(x=self.xcor(), y=self.ycor() + YPOS)

    def move_sud(self):
        self.goto(x=self.xcor(), y=self.ycor() - YPOS)
