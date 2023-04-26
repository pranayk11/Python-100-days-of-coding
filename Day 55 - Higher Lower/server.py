from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)


@app.route("/")
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess>")
def guess_number(guess):
    if guess < random_number:
        return '<h1 style="color: red">Too low, Try again!</h1>' \
               '<img src="https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif">'
    elif guess > random_number:
        return '<h1 style="color: purple">Too high, Try again!</h1>' \
               '<img src="https://media.giphy.com/media/l0MZkODdO27uuVLpu/giphy.gif">'
    else:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/naiba7cRbSjgrzJ9wa/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
