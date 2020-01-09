from flask import Flask


def create_app(config=None):
    """Create and return app."""
    app = Flask(__name__)
    load_blueprints(app)
    return app


def load_blueprints(app):
    from app.srv.routes import api
    from app.model.routes import api

    app.register_blueprint(srv.routes.api)
    app.register_blueprint(model.routes.api)

