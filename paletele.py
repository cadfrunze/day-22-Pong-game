from turtle import Turtle

STARTING_POS_PAL1 = ((500, 20), (500, 0), (500, -20), (500, -40))
STARTING_POS_PAL2 = ((-500, 20), (-500, 0), (-500, -20), (-500, -40))
MOVE_DISTANCE = 20


class Paleta(Turtle):
    """Creearea, pozitionarea, miscarea paletelor"""

    def __init__(self):
        super().__init__()
        self.segmente_dreapta = []
        self.segmente_stanga = []
        self.create_pal_st()
        self.create_pal_dr()
        self.starting_position(stanga=self.segmente_dreapta, dreapta=self.segmente_stanga)

    def create_pal_dr(self):
        for num in range(4):
            new_element = Turtle('square')
            new_element.color('yellow')
            new_element.penup()
            self.segmente_dreapta.append(new_element)

    def create_pal_st(self):
        for num in range(4):
            new_element = Turtle('square')
            new_element.color('green')
            new_element.penup()
            self.segmente_stanga.append(new_element)

    @staticmethod
    def starting_position(stanga, dreapta):
        pozitia_stanga = 0
        pozitia_dreapta = 0
        for position_st in STARTING_POS_PAL1:
            stanga[pozitia_stanga].goto(x=position_st[0], y=position_st[1])
            pozitia_stanga = pozitia_stanga + 1

        for position_dr in STARTING_POS_PAL2:
            dreapta[pozitia_dreapta].goto(x=position_dr[0], y=position_dr[1])
            pozitia_dreapta = pozitia_dreapta + 1

    def move_nord(self, lista_segmente):
        head = lista_segmente[0]
        obiectul = len(lista_segmente) - 1
        head.setheading(90)
        for element in lista_segmente[::-1]:
            element.setheading(90)
            if element == head:
                continue
            else:
                element.goto(x=lista_segmente[obiectul - 1].xcor(), y=lista_segmente[obiectul - 1].ycor())
                obiectul = obiectul - 1

        head.forward(MOVE_DISTANCE)

    def move_sud(self, lista_segmente):
        head = lista_segmente[-1]
        head.setheading(270)
        obiectul = 1
        for element in lista_segmente:
            if element == head:
                continue
            else:
                element.setheading(270)
                element.goto(x=lista_segmente[obiectul].xcor(), y=lista_segmente[obiectul].ycor())
                obiectul = obiectul + 1
        head.forward(MOVE_DISTANCE)

