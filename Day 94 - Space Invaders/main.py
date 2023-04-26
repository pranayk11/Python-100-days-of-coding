from turtle import Screen, Turtle
import time
import random

# Screen Setup
screen = Screen()
screen.setup(660, 660)
screen.title('Space Invaders')
screen.bgcolor('black')
screen.register_shape('images/space_ship.gif')
screen.register_shape('images/alien.gif')
screen.tracer(0)

# Draw Border
border = Turtle()
border.hideturtle()
border.color('white')
border.up()
border.goto(-280, -280)
border.down()
border.pensize(5)
for side in range(4):
    border.fd(560)
    border.left(90)

# Create Pen for Score
pen = Turtle()
pen.color('green')
pen.up()
pen.hideturtle()
pen.goto(220, -310)
pen.write('Score: 0', align='center', font=('Courier', 18, 'normal'))

# Create Pen to write title on Top
pen_title = Turtle()
pen_title.color('green')
pen_title.up()
pen_title.hideturtle()
pen_title.goto(0, 300)
pen_title.write('Space Invaders', align='center', font=('Courier', 20, 'bold'))

# Create Player Ship
player = Turtle()
player.shape('images/space_ship.gif')
# player.shape('triangle')
# player.color('blue')
player.up()
player.speed(0)
player.goto(0, -250)
player.left(90)
score = 0

# Create Bullet shot from Player Ship
bullet = Turtle()
bullet.color('yellow')
bullet.speed(0)
bullet.up()
bullet.shape('square')
bullet.shapesize(0.15, 0.6)
bullet.lt(90)
bullet.goto(-1000, -1000)    # Hide Bullet Off-Screen
bullet.state = 'ready'

# Create Enemy
enemy_list = []
enemy_speed = 0.5

x_list = [-200, -150, -100, -50, 0, 50, 100, 150, 200 ]
y_list = [250, 200, 150]

for i in x_list:
    for j in y_list:
        enemy = Turtle()
        enemy.shape('images/alien.gif')
        enemy.up()
        enemy.speed(0)
        enemy.goto(i, j)
        enemy.dx = enemy_speed
        enemy_list.append(enemy)

# Create torpedo dropped from the enemy
torpedo = Turtle()
torpedo.color('yellow')
torpedo.speed(0)
torpedo.up()
torpedo.shape('square')
torpedo.shapesize(0.15, 0.6)
torpedo.lt(90)
torpedo.goto(1000, 1000)    # Hide torpedo off-screen
laser = 'ready'


def move_left():
    """Player moves left if within border"""
    if player.xcor() >= -250:
        player.setx(player.xcor() - 20)


def move_right():
    """Player moves right if within border"""
    if player.xcor() <= 250:
        player.setx(player.xcor() + 20)


def move_enemy():
    for i in enemy_list:
        i.goto(i.xcor() + i.dx, i.ycor())

        if i.xcor() >= 260 or i.xcor() <= -260:
            # If enemy reaches the side, reverse and 30 pixels down
            for j in enemy_list:
                j.dx *= -1
                j.sety(j.ycor() - 30)


def shoot():
    """This is called when you press Space-bar"""
    if bullet.state == 'ready':
        bullet.goto(player.xcor(), player.ycor()+20)
        bullet.state = 'fire'


def enemy_laser():
    """ Fire torpedoes at player randomly"""
    global laser
    for i in enemy_list:
        x = random.random()  # Create probablity of firing torpedo only when laser == ready
        if x < 0.005 and laser == 'ready':
            laser = 'fire'
            torpedo.goto(i.xcor(), i.ycor() - 40)


def check_collision():
    """Hit the enemy ship"""
    global score
    for i in enemy_list:
        if bullet.distance(i) < 20:  #Check if bullet is less than 20 pixel from each enemy
            bullet.goto(1000, 1000)
            i.goto(1000, 1000)
            enemy_list.remove(i)
            score += 10
            pen.clear()
            pen.write(f"Score: {score}", align='center', font=('Courier', 18, 'normal'))


screen.listen()
screen.onkey(move_left, 'Left')
screen.onkey(move_right, 'Right')
screen.onkey(shoot, 'space')

game_over = False

"""MAIN GAME LOOP"""
while not game_over:
    screen.update()
    time.sleep(0.1)

    check_collision()  # Did you hit enemy with bullet
    move_enemy()  # Move enemies in a group to left, right and down
    enemy_laser()  # Shoot at player

    if bullet.state == 'fire':  # Every time you hit Space-bar
        if bullet.ycor() <= 260:
            bullet.sety(bullet.ycor()+20)
        else:
            bullet.goto(1000, 1000)  # Hide bullet off-screen
            bullet.state = 'ready'

    if laser == 'fire':  # Random fire from enemies
        if torpedo.ycor() >= -280:
            torpedo.sety(torpedo.ycor() - 20)
        else:
            torpedo.goto(1000, 1000)
            laser = 'ready'

    for i in enemy_list:
        if i.distance(player) <= 20 or i.ycor() < player.ycor():
            game_over = True

    if torpedo.distance(player) <= 20:
        game_over = True

    if len(enemy_list) == 0:
        # Reset the game
        game_over = True

print('Game Over')
pen.clear()
pen.goto(0, 0)
pen.write(f'Game Over\nScore: {score}', align='center', font=('Courier', 26, 'normal'))

screen.mainloop()
