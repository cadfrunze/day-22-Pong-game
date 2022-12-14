from turtle import Screen
from terenul import Terenul
from paletele import Paleta
from bila import Bila
from score import Scorul
import time

# Settings
screen = Screen()
screen.bgcolor('black')
screen.setup(width=1400, height=800)
screen.title(titlestring="Jocul")
scorul = Scorul()
screen.tracer(0)
screen.listen()
CULOARE_PAL_DR = "yellow"
POS_PAL_DR = (500, 0)
CULOARE_PAL_ST = "green"
POS_PAL_ST = (-500, 0)
terenul = Terenul()
bila = Bila()
paleta_dr = Paleta(position=POS_PAL_DR, culoarea=CULOARE_PAL_DR)
paleta_st = Paleta(position=POS_PAL_ST, culoarea=CULOARE_PAL_ST)


# Creearea functilor pt controale
def move_pal_nord_dr():
    if paleta_dr.ycor() == 240:
        screen.onkey(key="Down", fun=move_pal_sud_dr)
    else:
        paleta_dr.move_nord()


def move_pal_sud_dr():
    if paleta_dr.ycor() == -240:
        screen.onkey(key="Up", fun=move_pal_nord_dr)
    else:
        paleta_dr.move_sud()


def move_pal_nord_st():
    if paleta_st.ycor() == 240:
        screen.onkey(key="s", fun=move_pal_sud_st)
        screen.onkey(key="S", fun=move_pal_sud_st)
    else:
        paleta_st.move_nord()


def move_pal_sud_st():
    if paleta_st.ycor() == -240:
        screen.onkey(key="w", fun=move_pal_nord_st)
        screen.onkey(key="W", fun=move_pal_nord_st)
    else:
        paleta_st.move_sud()


# Creearea butoanelor de control


screen.onkey(key="Up", fun=move_pal_nord_dr)
screen.onkey(key="Down", fun=move_pal_sud_dr)
screen.onkey(key="w", fun=move_pal_nord_st)
screen.onkey(key="W", fun=move_pal_nord_st)
screen.onkey(key="s", fun=move_pal_sud_st)
screen.onkey(key="S", fun=move_pal_sud_st)
# # Joculbila.afisare_coordonate()
joc = True

# scorul.afisare_scor()
while joc:
    time.sleep(bila.move_speed)
    screen.update()
    bila.miscare_bila()
    # Detectarea cu peretii nord si sud
    if bila.ycor() > 280 or bila.ycor() < -280:
        bila.sari_inapoi()
    # Detect coliziunea cu paleta
    if bila.distance(paleta_dr) < 90 and bila.xcor() == 480:
        bila.sari_inapoi_paleta()
    if bila.distance(paleta_st) < 90 and bila.xcor() == -480:
        bila.sari_inapoi_paleta()
    # Detect cand bila trece de palete
    if bila.xcor() >= 530:
        screen.tracer(0)
        scorul.scor_st = scorul.scor_st + 1
        scorul.update_score(scor_dr=scorul.scor_dr, scor_st=scorul.scor_st)
        bila.reseteaza()
        screen.update()
    if bila.xcor() <= -530:
        screen.tracer(0)
        scorul.scor_dr = scorul.scor_dr + 1
        scorul.update_score(scor_dr=scorul.scor_dr, scor_st=scorul.scor_st)
        bila.reseteaza()
        screen.update()
screen.exitonclick()
