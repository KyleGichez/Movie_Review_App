from flask import Flask




def register_blueprints(app):
    """
    """
    from .main import main as main_bp
    app.register_blueprint(main_bp)

def create_app():
    """
    """
    app = Flask(__name__)
    register_blueprints(app)
    return app
