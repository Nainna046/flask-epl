from epl import create_app, db
from flask_migrate import Migrate

app = create_app()   # ⭐ สำคัญมาก ต้องเรียก create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
