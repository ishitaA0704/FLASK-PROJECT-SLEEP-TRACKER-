from track import db
class User(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    track = db.relationship('Sleep', backref='sleeper', lazy=True)

class Sleep(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    sleep_time = db.Column(db.String(20), nullable=False)
    wake_time = db.Column(db.String(20), nullable=False)
    duration = db.Column(db.String(20), nullable=False)
