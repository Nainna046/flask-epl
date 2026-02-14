from flask import Blueprint, redirect, render_template, url_for, flash, request
from epl import db
from epl.models import Club, Player

# ✅ สร้าง blueprint
main = Blueprint("main", __name__)


# ================================
# HOME
# ================================
@main.route('/')
def index():
    return render_template('index.html', title='Home Page')


# ================================
# CLUBS MODULE
# ================================
@main.route('/clubs')
def all_clubs():
    clubs = db.session.scalars(db.select(Club)).all()
    return render_template(
        'clubs/index.html',
        title='Clubs Page',
        clubs=clubs
    )


@main.route('/clubs/new', methods=['GET', 'POST'])
def new_club():
    if request.method == 'POST':
        name = request.form['name']
        stadium = request.form['stadium']
        year = int(request.form['year'])
        logo = request.form['logo']

        club = Club(name=name, stadium=stadium, year=year, logo=logo)
        db.session.add(club)
        db.session.commit()

        flash('add new club successfully', 'success')
        return redirect(url_for('main.all_clubs'))

    return render_template(
        'clubs/new_club.html',
        title='New Club Page'
    )


@main.route('/clubs/search', methods=['GET', 'POST'])
def search_club():
    if request.method == 'POST':
        club_name = request.form['club_name']
        clubs = db.session.scalars(
            db.select(Club).where(Club.name.like(f'%{club_name}%'))
        ).all()

        return render_template(
            'clubs/search_club.html',
            title='Search Club Page',
            clubs=clubs
        )

    return render_template(
        'clubs/search_club.html',
        title='Search Club Page',
        clubs=[]
    )


@main.route('/clubs/<int:id>/info')
def info_club(id):
    club = db.session.get(Club, id)
    return render_template(
        'clubs/info_club.html',
        title='Info Club Page',
        club=club
    )


@main.route('/clubs/<int:id>/update', methods=['GET', 'POST'])
def update_club(id):
    club = db.session.get(Club, id)

    if request.method == 'POST':
        club.name = request.form['name']
        club.stadium = request.form['stadium']
        club.year = int(request.form['year'])
        club.logo = request.form['logo']

        db.session.commit()

        flash('update club successfully', 'success')
        return redirect(url_for('main.all_clubs'))

    return render_template(
        'clubs/update_club.html',
        title='Update Club Page',
        club=club
    )


# ================================
# PLAYERS MODULE
# ================================
@main.route('/players')
def all_players():
    players = db.session.scalars(db.select(Player)).all()
    return render_template(
        'players/index.html',
        title='Players Page',
        players=players
    )


@main.route('/players/new', methods=['GET', 'POST'])
def new_player():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        nationality = request.form['nationality']
        club_id = int(request.form['club_id'])

        # ✅ clean sheets (กัน crash)
        clean_sheets = request.form.get('clean_sheets')
        try:
            clean_sheets = int(clean_sheets) if clean_sheets else None
        except ValueError:
            clean_sheets = None

        player = Player(
            name=name,
            position=position,
            nationality=nationality,
            clean_sheets=clean_sheets,
            club_id=club_id
        )

        db.session.add(player)
        db.session.commit()

        flash('add new player successfully', 'success')
        return redirect(url_for('main.all_players'))

    clubs = db.session.scalars(db.select(Club)).all()
    return render_template(
        'players/new_player.html',
        title='New Player Page',
        clubs=clubs
    )


@main.route('/players/<int:id>/info')
def info_player(id):
    player = db.session.get(Player, id)
    return render_template(
        'players/info_player.html',
        title='Info Player Page',
        player=player
    )


@main.route('/players/<int:id>/update', methods=['GET', 'POST'])
def update_player(id):
    player = db.session.get(Player, id)

    if request.method == 'POST':
        player.name = request.form['name']
        player.position = request.form['position']
        player.nationality = request.form['nationality']
        player.club_id = int(request.form['club_id'])

        # ✅ clean sheets (กัน crash)
        clean_sheets = request.form.get('clean_sheets')
        try:
            player.clean_sheets = int(clean_sheets) if clean_sheets else None
        except ValueError:
            player.clean_sheets = None

        db.session.commit()

        flash('update player successfully', 'success')
        return redirect(url_for('main.all_players'))

    clubs = db.session.scalars(db.select(Club)).all()
    return render_template(
        'players/update_player.html',
        title='Update Player Page',
        player=player,
        clubs=clubs
    )
