from turtle import Screen, Turtle
import random
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1200, height=800)
screen.title(titlestring="Joc in teste")
screen.listen()
screen.tracer(0)
t2 = Turtle()
t2.penup()
t2.hideturtle()
t2.goto(x=-580, y=-300)
t2.color('white')
t2.pendown()
t2.pensize(5)
t2.forward(1160)
t2.setheading(90)
t2.forward(600)
t2.setheading(180)
t2.forward(1160)
t2.setheading(270)
t2.forward(600)
t1 = Turtle('circle')
t1.color('blue')
# t1.penup()
lista_obiecte = []
obiect_miscare = {}
lista_culori = ['red', 'blue', 'yellow', 'white', 'green', 'purple', 'pink']
lista_unghiuri = []
alegere_numar = int(screen.textinput(title="Alegere numar obiecte", prompt="Alege numar obiecte"))
unghi = 0
for obiect in range(alegere_numar):
    obiectul = Turtle('circle')
    obiectul.color(random.choice(lista_culori))
    obiectul.setheading(unghi)
    obiectul.penup()
    obiect_miscare["obiectul"] = obiectul
    lista_obiecte.append(obiect_miscare)

for numar in range(alegere_numar):
    numar1 = random.randint(1, 350)
    while numar1 == 90 or numar1 == 180:
        numar1 = random.randint(1, 350)
    lista_unghiuri.append(numar1)
print(lista_unghiuri)
provizoriu = 0
for atribuire in lista_unghiuri:
    lista_obiecte[provizoriu]['unghi'] = lista_unghiuri[provizoriu]
    provizoriu = provizoriu + 1




print(lista_obiecte)
MOVE_DISTANCE = 1
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0
# lungimea = 580
# latimea = 300

joc = True
while joc:
    time.sleep(0.001)
    screen.update()
    for obiect_miscare in lista_obiecte:
        obiect_miscare["obiectul"].forward(int(MOVE_DISTANCE))
        # print(f"xcor(): {int(obiect_miscare['obiectul'].xcor())}")
        # print(f"ycor(): {int(obiect_miscare.ycor())}")
        if int(obiect_miscare['obiectul'].xcor()) >= 560 or int(obiect_miscare['obiectul'].xcor()) <= -560:
            screen.tracer()
            obiect_miscare["unghi"] = 180 - obiect_miscare["unghi"]
            obiect_miscare['obiectul'].setheading(obiect_miscare["unghi"])
            obiect_miscare['obiectul'].forward(MOVE_DISTANCE)
            time.sleep(0.001)
            screen.update()

        elif int(obiect_miscare['obiectul'].ycor()) >= 285 or int(obiect_miscare['obiectul'].ycor()) <= -285:
            screen.tracer()
            obiect_miscare["unghi"] = 360 - obiect_miscare["unghi"]
            obiect_miscare['obiectul'].setheading(obiect_miscare["unghi"])
            obiect_miscare['obiectul'].forward(MOVE_DISTANCE)
            time.sleep(0.001)
            screen.update()










screen.exitonclick()