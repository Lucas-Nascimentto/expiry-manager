from flask import Flask
from .config import Config
from .extensions import db, migrate
from .models import product, batch, user

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)

    return app