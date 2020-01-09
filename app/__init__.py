from flask import Flask


def create_app(config=None):
    """Create and return app."""
    app = Flask(__name__)
    load_blueprints(app)
    return app


def load_blueprints(app):
    from app.srv.routes import api

    app.register_blueprint(app.srv.routes.society_info)
