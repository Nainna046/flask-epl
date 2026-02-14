from flask import Blueprint, render_template

# ⭐ main blueprint สำหรับหน้าแรก
main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("core/index.html")


