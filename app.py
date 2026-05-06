from track import app, db
from track.models import Sleep

with app.app_context():
    db.create_all()
    

if __name__ == "__main__":
    app.run()

