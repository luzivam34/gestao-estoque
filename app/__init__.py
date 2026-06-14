#Bibliotecas
from flask import Flask
from app.extension_service.extension_service import db,mg
from config import Config

#funcão do app
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mg.init_app(app, db)


    #route imports
    from .routes.main_routes import main_bp
    from .routes.produto_route import produto_bp

    # routes register
    app.register_blueprint(main_bp)
    app.register_blueprint(produto_bp)

    with app.app_context():
        db.create_all()

    return app
