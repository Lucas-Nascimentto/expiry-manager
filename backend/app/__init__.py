from flask import Flask
from .config import Config
from .extensions import db, migrate
from .models import product, batch, user
from .routes.product_routes import product_bp
from .routes.batch_routes import batch_bp
from .routes.auth_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(product_bp)
    app.register_blueprint(batch_bp)
    app.register_blueprint(user_bp)

    return app