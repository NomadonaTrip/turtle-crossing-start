from turtle import Turtle

FONT = ("Courier", 18, "normal")
ENDGAME_FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x= -260, y = 250)
        self.write(f"Level: {self.level}", False, font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(arg= f"Level: {self.level}", move= False, font= FONT)

    def end_game(self):
        self.goto(x= 0, y = 0)
        self.write(arg = "Game Over", align= 'center', font = ENDGAME_FONT)




