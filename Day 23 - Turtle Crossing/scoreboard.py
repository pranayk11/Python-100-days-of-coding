from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Displays the scoreboard."""
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        """Increase level when player crosses finish line."""
        self.level += 1

    def game_over(self):
        """Shows Game over when player touches the car."""
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

