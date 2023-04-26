from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from colorthief import ColorThief
import os

app = Flask(__name__)

upload_folder = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = 'static/images/'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/result", methods=["GET", "POST"])
def result():
    file = request.files['file']
    print(file.filename)
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    full_img_path = f"static/images/{file.filename}"
    color_thief = ColorThief(full_img_path)
    top_colors = color_thief.get_palette(quality=11)
    return render_template('result.html', img=full_img_path, top_colors=top_colors)


if __name__ == '__main__':
    app.run(debug=True)
