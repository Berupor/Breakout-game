from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(410, 410)
        self.write(f'Lives:{self.lives}', align="left", font=("Courier", 30, "normal"))

    def minus_live(self):
        self.lives -= 1
        self.update_scoreboard()

    def scoreboard_refresh(self):
        self.lives = 3
        self.update_scoreboard()
