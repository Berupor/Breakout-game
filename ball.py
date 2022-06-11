from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.y = -300
        self.x = 0
        self.length_x = 2   # length of move
        self.length_y = 2   # length of move
        self.move_speed = 0.00000001

    def moving(self):
        self.x += self.length_x
        self.y += self.length_y
        self.goto(x=self.x, y=self.y)

    def crash_vertically(self):
        """Reverse moving"""
        self.length_y = -self.length_y

    def crash_with_wall(self):
        if self.x < 0:
            self.length_x = -self.length_x
        elif self.x > 0:
            self.length_x = -self.length_x

    def ball_refresh(self):
        self.y = -300
        self.x = 0
        self.length_x = 2
        self.length_y = 2
