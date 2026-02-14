from flask import Blueprint, redirect, render_template, url_for, flash, request
from epl import db
from epl.models import Club, Player

# ✅ blueprint
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
    q = request.args.get('q')

    stmt = db.select(Club)

    # 🔍 search
    if q:
        stmt = stmt.where(Club.name.ilike(f"%{q}%"))

    clubs = db.session.scalars(stmt).all()

    return render_template(
        'clubs/index.html',
        title='Clubs Page',
        clubs=clubs
    )


@main.route('/clubs/new', methods=['GET', 'POST'])
def new_club():
    if request.method == 'POST':
        club = Club(
            name=request.form['name'],
            city=request.form['city'],
            founded=int(request.form['founded']),
            logo=request.form.get('logo')
        )

        db.session.add(club)
        db.session.commit()

        flash('add new club successfully', 'success')
        return redirect(url_for('main.all_clubs'))

    return render_template(
        'clubs/new_club.html',
        title='New Club Page'
    )


# 👁 info club
@main.route('/clubs/<int:id>/info')
def info_club(id):
    club = db.session.get(Club, id)
    return render_template(
        'clubs/info_club.html',
        title='Info Club Page',
        club=club
    )


# ✏️ update
@main.route('/clubs/<int:id>/update', methods=['GET', 'POST'])
def update_club(id):
    club = db.session.get(Club, id)

    if request.method == 'POST':
        club.name = request.form['name']
        club.city = request.form['city']
        club.founded = int(request.form['founded'])
        club.logo = request.form.get('logo')

        db.session.commit()

        flash('update club successfully', 'success')
        return redirect(url_for('main.all_clubs'))

    return render_template(
        'clubs/update_club.html',
        title='Update Club Page',
        club=club
    )


# 🗑 DELETE (สำคัญมาก)
@main.route('/clubs/<int:id>/delete', methods=['POST'])
def delete_club(id):
    club = db.session.get(Club, id)

    if club:
        db.session.delete(club)
        db.session.commit()
        flash('delete club successfully', 'success')

    return redirect(url_for('main.all_clubs'))

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
        clean_sheets = request.form.get('clean_sheets')
        try:
            clean_sheets = int(clean_sheets) if clean_sheets else None
        except ValueError:
            clean_sheets = None

        player = Player(
            name=request.form['name'],
            position=request.form['position'],
            nationality=request.form['nationality'],
            clean_sheets=clean_sheets,
            club_id=int(request.form['club_id'])
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
