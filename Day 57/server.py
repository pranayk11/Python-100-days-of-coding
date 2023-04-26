from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home_page():
    random_number = random.randint(1, 10)
    today = datetime.datetime.now()
    year = today.strftime('%Y')
    return render_template("index.html", num=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    age_url = f"https://api.agify.io/?name={name}"
    agify_response = requests.get(age_url)
    agify_data = agify_response.json()
    age = agify_data["age"]

    gender_url = f"https://api.genderize.io/?name={name}"
    genderize_response = requests.get(gender_url)
    genderize_data = genderize_response.json()
    gender = genderize_data["gender"]
    return render_template("guess.html", person_name=name, gender=gender, age=age)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/9e2d78681bfd0cbd477a"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
