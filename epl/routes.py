from flask import Blueprint, render_template
from . import db
from .models import Club

main = Blueprint("main", __name__)

@main.route("/")
def index():
    clubs = Club.query.all()
    return render_template("clubs.html", clubs=clubs)

@main.route("/add")
def add_clubs():
    clubs = [
        Club(
            name="Arsenal",
            stadium="Emirates Stadium",
            founded=1886,
            logo="https://resources.premierleague.com/premierleague/badges/25/t3.png"
        ),
        Club(
            name="Aston Villa",
            stadium="Villa Park",
            founded=1874,
            logo="https://resources.premierleague.com/premierleague/badges/25/t7.png"
        ),
        Club(
            name="Bournemouth",
            stadium="Vitality Stadium",
            founded=1899,
            logo="https://resources.premierleague.com/premierleague/badges/25/t91.png"
        ),
    ]

    db.session.add_all(clubs)
    db.session.commit()
    return "Added Premier League clubs!"
