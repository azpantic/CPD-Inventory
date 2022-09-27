from flaskr.app import app
from flask import render_template, redirect, url_for
from flask_login import current_user

@app.route("/")
def init():
    return redirect(url_for("index"))

@app.route("/index")
def index():
    # print(current_user.is_authenticated)
    return render_template("index.html")