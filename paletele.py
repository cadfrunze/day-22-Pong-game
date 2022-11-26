from turtle import Turtle

STARTING_POS_PAL1 = ((-400, 20), (-400, 0), (-400, -20), (-400, -40))
STARTING_POS_PAL2 = ((400, 20), (400, 0), (400, -20), (400, -40))


class Paleta(Turtle):
    def __init__(self):
        super().__init__()
        self.segmente_stanga = []
        self.segmente_dreapta = []
        self.create_pal_st()
        self.create_pal_dr()
        self.starting_position(stanga=self.segmente_stanga, dreapta=self.segmente_dreapta)


    def create_pal_st(self):
        for num in range(4):
            new_element = Turtle('square')
            new_element.color('white')
            new_element.penup()
            self.segmente_stanga.append(new_element)

    def create_pal_dr(self):
        for num in range(4):
            new_element = Turtle('square')
            new_element.color('white')
            new_element.penup()
            self.segmente_dreapta.append(new_element)

    def starting_position(self, stanga, dreapta):
        pozitia_stanga = 0
        pozitia_dreapta = 0
        for position_st in STARTING_POS_PAL1:
            stanga[pozitia_stanga].goto(x=position_st[0], y=position_st[1])
            pozitia_stanga = pozitia_stanga + 1

        for position_dr in STARTING_POS_PAL2:
            dreapta[pozitia_dreapta].goto(x=position_dr[0], y=position_dr[1])
            pozitia_dreapta = pozitia_dreapta + 1



