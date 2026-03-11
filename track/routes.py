from track import app
from flask import render_template
from track.models import Sleep
from track.log import LoginForm


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def Login():
    form = LoginForm()
    return render_template("Login.html", form=form)

@app.route("/track")
def Track():
    sleep_data = Sleep.query.all()
    return render_template("Tracker.html", sleep_data=sleep_data)