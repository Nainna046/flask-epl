from . import db


class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    stadium = db.Column(db.String(100))
    founded = db.Column(db.Integer)
    logo = db.Column(db.String(255))

    players = db.relationship("Player", backref="club", lazy=True)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    position = db.Column(db.String(50))
    nationality = db.Column(db.String(50))
    photo = db.Column(db.String(255))

    club_id = db.Column(db.Integer, db.ForeignKey("club.id"))
