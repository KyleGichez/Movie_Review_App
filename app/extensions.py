"""
Extensions imports.
"""
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

"""
Create named variables pointing to the package.
These `named package variables` can be imported by any module,
and then used to access any functionality offered by the package.
"""
cors = CORS()
db = SQLAlchemy()

def register_extensions(app):
    """
    All application extensions will be initiated with 
    the app instance from this container.

    -   We use the method `init_app` to initialize 
        the package with the application context. The
        syntax looks like `<package>.init_app(app)`.


    """
    cors.init_app(app)
    db.init_app(app)
