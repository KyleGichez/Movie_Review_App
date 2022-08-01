# pip package imports
from flask import Flask

# custom code imports
from .extensions import register_extensions


def register_blueprints(app):
    """
    Blueprints registration.
    Blueprints are modular parts of the application.
    They have to be registered, so that the flask app can pick them up.
    """
    # main blueprint : contains home page and most likely any route that does not need authentication.
    from .main import main as main_bp
    app.register_blueprint(main_bp)

def create_app():
    """
    A function that creates an application instance.
    """
    app = Flask(__name__)
    register_blueprints(app)
    register_extensions(app)
    return app
