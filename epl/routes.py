from flask import Blueprint, render_template, request
from .models import Club, Player

main = Blueprint("main", __name__)


@main.route("/")
def clubs():
    clubs = Club.query.all()
    return render_template("clubs/index.html", clubs=clubs)


@main.route("/clubs/<int:club_id>")
def club_info(club_id):
    club = Club.query.get_or_404(club_id)
    players = Player.query.filter_by(club_id=club.id).all()

    return render_template(
        "clubs/info_club.html",
        club=club,
        players=players
    )


@main.route("/clubs/search")
def search_club():
    keyword = request.args.get("q", "")
    clubs = Club.query.filter(
        Club.name.ilike(f"%{keyword}%")
    ).all()

    return render_template("clubs/index.html", clubs=clubs)
