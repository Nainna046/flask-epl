from . import db

class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    stadium = db.Column(db.String(100), nullable=False)
    founded = db.Column(db.Integer, nullable=False)
    logo = db.Column(db.String(255), nullable=False)
