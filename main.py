import time
from turtle import Screen, Turtle
from stick import Stick
from ball import Ball
from blocks import Blocks
from scoreboard import Scoreboard

screen = Screen()
screen.colormode(255)
screen.bgcolor('black')
screen.setup(width=1100, height=900)
screen.title('Breakout')
screen.tracer(0)

turtle_text = Turtle()
turtle_text.hideturtle()
turtle_text.penup()
turtle_text.color('white')

stick = Stick()
ball = Ball()
scoreboard = Scoreboard()
blocks = Blocks()

screen.listen()
screen.onkey(stick.to_left, "Left")
screen.onkey(stick.to_right, "Right")

game_is_on = False
turtle_text.write('"Space" to start and Restart', font=("Arial", 50, "normal"), align='center')


def start_game():
    global game_is_on
    game_is_on = True
    scoreboard.scoreboard_refresh()
    blocks.blocks_refresh()
    blocks.create_block(3)
    ball.ball_refresh()
    screen.update()
    turtle_text.clear()

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.moving()

        if ball.ycor() > 440:
            ball.crash_vertically()
        elif ball.xcor() > 530 or ball.xcor() < -540:
            ball.crash_with_wall()

        elif ball.distance(stick) < 50 and ball.ycor() < -380:
            ball.crash_vertically()

        elif ball.ycor() < -450:
            ball.ball_refresh()
            scoreboard.minus_live()

        for block in blocks.all_blocks:
            if ball.distance(block) < 40:
                ball.crash_vertically()
                block.hideturtle()
                block_index = blocks.all_blocks.index(block)
                blocks.delete_block(block_index)

        if scoreboard.lives == 0:
            turtle_text.write('You lose! Press "Space" to restart', font=("Arial", 50, "normal"), align='center')
            game_is_on = False
        elif len(blocks.all_blocks) == 0:
            turtle_text.write('You Win! Press "Space" to restart', font=("Arial", 50, "normal"), align='center')
            game_is_on = False


screen.onkey(start_game, 'space')

screen.exitonclick()
