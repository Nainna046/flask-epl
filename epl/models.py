from . import db


class Club(db.Model):
    __tablename__ = "clubs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    founded = db.Column(db.Integer)

    players = db.relationship("Player", backref="club", lazy=True)


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    position = db.Column(db.String(50))
    nationality = db.Column(db.String(50))

    # ⭐ ต้องมีอันนี้ตามโจทย์
    clean_sheets = db.Column(db.Integer, nullable=True)

    club_id = db.Column(db.Integer, db.ForeignKey("clubs.id"))

