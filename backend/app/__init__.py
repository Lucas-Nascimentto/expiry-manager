from flask import Flask
from .config import Config
from .extensions import db, migrate, cors, bcrypt
from .models import product, batch, user
from .routes.product_routes import product_bp
from .routes.batch_routes import batch_bp
from .routes.user_routes import user_bp
from .routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(product_bp)
    app.register_blueprint(batch_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)

    return app