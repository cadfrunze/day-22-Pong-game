from turtle import Turtle


class Scorul(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.user_dr = ""
        self.user_st = ""
        self.scor_dr = 0
        self.scor_st = 0

    def innregistrare_useri(self):
        user1 = self.user_dr = self.screen.textinput(title="Innregistrare user dreapta",
                                                     prompt="Scrie un nume").capitalize()
        self.user_dr = user1
        user2 = self.user_st = self.screen.textinput(title="Innregistrare user stanga",
                                                     prompt="Scrie al doilea nume").capitalize()
        self.user_st = user2

    def afisare_scor(self):
        self.goto(x=24, y=310)
        self.write(arg=f"{self.user_st}:  {self.scor_st}" + 2 * " " + "|" + 2 * " " + f"{self.scor_dr}" + 3 * " " + f":{self.user_dr}",
                   align="center", font=("Arial", 20, "bold"))
