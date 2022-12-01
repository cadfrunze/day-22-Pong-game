from turtle import Screen, Turtle
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

# Create paleta dreapta
paleta_dr = Turtle('square')
paleta_dr.penup()
paleta_dr.color('yellow')
paleta_dr.shapesize(stretch_wid=5, stretch_len=1)
paleta_dr.goto(x=500, y=0)

# Create paleta stanga
paleta_st = Turtle('square')
paleta_st.penup()
paleta_st.color('green')
paleta_st.shapesize(stretch_wid=5, stretch_len=1)
paleta_st.goto(x=-500, y=0)

YPOS = 20


def move_pal_dr_nord():
    print(paleta_dr.ycor())
    if paleta_dr.ycor() == 240:
        screen.onkey(key="Down", fun=move_pal_dr_sud)
    else:
        paleta_dr.goto(x=500, y=paleta_dr.ycor() + YPOS)


def move_pal_dr_sud():
    if paleta_dr.ycor() == -240:
        screen.onkey(key="Up", fun=move_pal_dr_nord)
    else:
        paleta_dr.goto(x=500, y=paleta_dr.ycor() - YPOS)


def move_pal_st_nord():
    if paleta_st.ycor() == 240:
        screen.onkey(key="s", fun=move_pal_st_sud)
        screen.onkey(key="S", fun=move_pal_st_sud)
    else:
        paleta_st.goto(x=-500, y=paleta_st.ycor() + YPOS)


def move_pal_st_sud():
    if paleta_st.ycor() == -240:
        screen.onkey(key="W", fun=move_pal_st_nord)
        screen.onkey(key="s", fun=move_pal_st_sud)
    else:
        paleta_st.goto(x=-500, y=paleta_st.ycor() - YPOS)


screen.onkey(key="Up", fun=move_pal_dr_nord)
screen.onkey(key="Down", fun=move_pal_dr_sud)
screen.onkey(key="w", fun=move_pal_st_nord)
screen.onkey(key="W", fun=move_pal_st_nord)
screen.onkey(key="s", fun=move_pal_st_sud)
screen.onkey(key="S", fun=move_pal_st_sud)
# # Jocul
joc = True

while joc:
    screen.update()
    time.sleep(0.003)

screen.exitonclick()
