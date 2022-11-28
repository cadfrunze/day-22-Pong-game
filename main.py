from turtle import Screen
from paletele import Paleta
from terenul import Terenul
from bila import Bila
import time

# Settings
screen = Screen()
screen.bgcolor('black')
screen.setup(width=1400, height=800)
screen.title(titlestring="Jocul")
screen.tracer(0)
screen.listen()
terenul = Terenul()
paleta = Paleta()
bila = Bila()


# Creearea functii butoane
def move_nord_pal_dr():
    if int(paleta.segmente_dreapta[0].ycor()) == 280:
        screen.onkey(key="Down", fun=move_sud_pal_dr)

    else:
        paleta.move_nord(lista_segmente=paleta.segmente_dreapta)


def move_nord_pal_st():
    if int(paleta.segmente_stanga[0].ycor()) == 280:
        screen.onkey(key="s", fun=move_sud_pal_st)
    else:
        paleta.move_nord(lista_segmente=paleta.segmente_stanga)


def move_sud_pal_dr():
    if int(paleta.segmente_dreapta[-1].ycor()) == -280:
        screen.onkey(key="Up", fun=move_nord_pal_dr)

    else:
        paleta.move_sud(lista_segmente=paleta.segmente_dreapta)


def move_sud_pal_st():
    if int(paleta.segmente_stanga[-1].ycor() == -280):
        screen.onkey(key="w", fun=move_nord_pal_st)
    else:
        paleta.move_sud(lista_segmente=paleta.segmente_stanga)


# Creeare butoane
screen.onkey(key="Up", fun=move_nord_pal_dr)
screen.onkey(key="w", fun=move_nord_pal_st)
screen.onkey(key="W", fun=move_nord_pal_st)
screen.onkey(key="Down", fun=move_sud_pal_dr)
screen.onkey(key="s", fun=move_sud_pal_st)
screen.onkey(key="S", fun=move_sud_pal_st)
# Jocul
joc = True
bila.verificare()
while joc:
    screen.update()
    bila.verificare()
    time.sleep(0.001)
    print(int(bila.ycor()))
screen.exitonclick()
