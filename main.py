from turtle import Screen
from paletele import Paleta
from terenul import Terenul
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1400, height=800)
screen.title(titlestring="Jocul")
screen.tracer(0)
screen.listen()
terenul = Terenul()
paleta = Paleta()


def move_nord_pal_dr():
    paleta.move_nord(lista_segmente=paleta.segmente_dreapta)


def move_nord_pal_st():
    paleta.move_nord(lista_segmente=paleta.segmente_stanga)


def move_sud_pal_dr():
    paleta.move_sud(lista_segmente=paleta.segmente_dreapta)


def move_sud_pal_st():
    paleta.move_sud(lista_segmente=paleta.segmente_stanga)


screen.onkey(key="Up", fun=move_nord_pal_dr)
screen.onkey(key="w", fun=move_nord_pal_st)
screen.onkey(key="Down", fun=move_sud_pal_dr)
screen.onkey(key="s", fun=move_sud_pal_st)

joc = True
while joc:
    time.sleep(0.01)
    screen.update()

screen.exitonclick()
