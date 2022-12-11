from turtle import Turtle


class Scorul(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.user_dr = ""
        self.user_st = ""
        self.innregistrare_useri()
        self.grosimea = (10 * len(self.user_st)) + (8 * 10)
        self.goto(x=(-1 * self.grosimea), y=310)
        self.scor_dr = 0
        self.scor_st = 0
        self.afisare_scor()

    def innregistrare_useri(self):
        user1 = self.user_dr = self.screen.textinput(title="Innregistrare user dreapta",
                                                     prompt="Scrie un nume").capitalize()
        self.user_dr = user1
        user2 = self.user_st = self.screen.textinput(title="Innregistrare user stanga",
                                                     prompt="Scrie al doilea nume").capitalize()
        self.user_st = user2

    def update_score(self, scor_st, scor_dr):
        self.scor_st = scor_st
        self.scor_dr = scor_dr
        self.clear()
        self.afisare_scor()

    def afisare_scor(self):
        self.write(
            arg=f"{self.user_st} : {self.scor_st}  |  {self.scor_dr} : {self.user_dr}",
            font=("Arial", 20, "bold"))
