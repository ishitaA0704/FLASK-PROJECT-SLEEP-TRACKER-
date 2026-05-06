from track import app
from flask import flash, render_template, request, redirect, url_for
from track import db
from track.models import Sleep
from track.log import LoginForm


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def Login():
    form = LoginForm()

    if form.validate_on_submit():

        # check if user already exists
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            flash("User already exists!", category="danger")
        else:
            new_user = User(
                name=form.name.data,
                email=form.email.data,
                password=form.password1.data
            )

            db.session.add(new_user)
            db.session.commit()

            flash("Account created successfully!", category="success")
            return redirect(url_for('home'))

    return render_template("Login.html", form=form)

@app.route("/track", methods=["GET", "POST"])
def Track():
    if request.method == "POST":
        date = request.form.get("date")
        sleeptime = request.form.get("sleeptime")
        waketime = request.form.get("waketime")

        duration = "Not calculated"

        new_sleep = Sleep(
            date=date,
            sleeptime=sleeptime,
            waketime=waketime,
            duration=duration,
            user_num=1   
        )

        db.session.add(new_sleep)
        db.session.commit()

        return redirect(url_for('Track'))

    sleep_data = Sleep.query.all()
    return render_template("Tracker.html", sleep_data=sleep_data)