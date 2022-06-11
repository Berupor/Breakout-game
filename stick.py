from turtle import Turtle


class Stick(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.turtlesize(stretch_wid=0.3, stretch_len=5)
        self.y = -400
        self.x = 0
        self.goto(x=self.x, y=self.y)

    def to_right(self):
        self.x += 20
        self.goto(self.x, self.y)

    def to_left(self):
        self.x -= 20
        self.goto(self.x, self.y)