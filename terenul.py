from turtle import Turtle


class Terenul(Turtle):
    """Creearea, trasarea marcajelor + fileu"""

    def __init__(self):
        super().__init__()
        self.t2 = Turtle()
        self.t2.penup()
        self.t2.hideturtle()
        self.t2.goto(x=-560, y=-300)
        self.t2.color('white')
        self.t2.pendown()
        self.t2.pensize(5)
        self.marcajele()
        self.peretele_nord = 291
        self.peretele_sud = -291
        self.peretele_dr, self.peretele_st = 560, -560

    def marcajele(self):
        for _ in range(4):
            self.t2.forward(1125)
            self.t2.left(90)
            self.t2.forward(600)
            self.t2.left(90)
        self.t2.goto(x=0, y=-300)
        self.t2.left(90)
        self.t2.color('blue')
        self.t2.penup()
        self.t2.forward(5)
        for i in range(30):
            self.t2.pendown()
            self.t2.forward(10)
            self.t2.penup()
            self.t2.forward(10)
