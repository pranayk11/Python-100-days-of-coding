from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import ScoreBoard
import time

screen = Screen()
paddle = Paddle((0, -270))
ball = Ball()
scoreboard = ScoreBoard()

# Game Screen
screen.bgcolor('black')
screen.setup(width=500, height=600)
screen.title('Breakout Game')
# screen.tracer(0)   # Turns off game animations

# Assign Key Strokes
screen.listen()
screen.onkey(paddle.go_left, "a")
screen.onkey(paddle.go_right, "d")

# Creating bricks wall
bricks_x_axis = -230
bricks_y_axis = 240
bricks = []

for i in range(7):
    for j in range(10):
        brick = Brick((bricks_x_axis, bricks_y_axis))
        bricks.append(brick)
        bricks_x_axis += 50
    bricks_x_axis = -230
    bricks_y_axis -= 20

# Main Game
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with left and right wall. Change the ball direction (bounce)
    if ball.xcor() > 230 or ball.xcor() < -230:
        ball.bounce_wall()

    # Detect collision with top wall. Change the ball direction
    if ball.ycor() > 240:
        ball.bounce_paddle()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -250:
        ball.bounce_paddle()

    # Detect if ball misses the paddle
    if ball.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with Bricks
    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce_wall()
            brick.hideturtle()
            x_axis_difference = ball.distance(brick)
            y_axis_difference = ball.distance(brick)
            if x_axis_difference > y_axis_difference:
                # If ball ditches at the side of the brick then ball x-axis will be switched
                ball.bounce_wall()
            else:
                # If the ball ditches at the top or bottom of the brick then ball's y-axis wwill be switched
                ball.bounce_wall()
                ball.bounce_paddle()
            bricks.remove(brick)
            scoreboard.points()
            if scoreboard.get_score() % 100 == 0:
                ball.increase_speed()
            break

    if not bricks:
        is_game_on = False
        scoreboard.win()


screen.exitonclick()
