# main.py

import os
from flask import Flask, render_template

app = Flask(__name__)

IMAGE_FOLDER = "static/images"

def get_images():
    if not os.path.exists(IMAGE_FOLDER):
        os.makedirs(IMAGE_FOLDER)

    files = os.listdir(IMAGE_FOLDER)
    images = [f for f in files if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    return images

@app.route("/")
def gallery():
    images = get_images()
    return render_template("gallery.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)
