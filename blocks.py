from turtle import Turtle
import random


def change_color():
    R = random.randrange(100, 257, 100)
    G = random.randrange(100, 257, 100)
    B = random.randrange(100, 257, 100)
    return R, G, B


class Blocks(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.y = 300
        self.x = 485
        self.all_blocks = []

    def create_block(self, rows):
        if rows != 0:
            for block in range(13):
                block = Turtle()
                block.color(change_color())
                block.shape('square')
                block.turtlesize(stretch_wid=2, stretch_len=4)
                block.penup()
                block.goto(x=self.x, y=self.y)
                self.x -= 82
                self.all_blocks.append(block)
            self.x = 485
            self.y -= 50
            self.create_block(rows=rows - 1)

    def delete_block(self, block):
        self.all_blocks.pop(block)

    def blocks_refresh(self):
        for block in self.all_blocks:
            block.hideturtle()
        self.all_blocks.clear()
        self.y = 300
