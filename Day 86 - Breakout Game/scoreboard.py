from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(self.score, align='center', font=("Courier", 20, 'normal'))

    def points(self):
        self.score += 10
        self.update_scoreboard()

    def get_score(self):
        return self.score

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=("Courier", 30, 'normal'))

    def win(self):
        self.goto(0, 0)
        self.write("YOU WIN!!", align='center', font=("Courier", 30, 'normal'))
