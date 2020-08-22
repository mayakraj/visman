from flask import Flask
from flask_bcrypt import Bcrypt
import os
from flask_cors import CORS
from flask_mail import Mail

#from peewee import PostgresqlDatabase

from flask_bcrypt import Bcrypt

SECRET_KEY = 'vis'
SECURITY_PASSWORD_SALT = 'vis'

def load_blueprints(app):
    from vis_app.routes.server import server
    from vis_app.routes.user import user
    from vis_app.routes.flat import flat
    from vis_app.routes.society import society
    from vis_app.routes.visitor import visitor
    from vis_app.routes.dashboard import dashboard

    app.register_blueprint(server)
    app.register_blueprint(user)
    app.register_blueprint(society)
    app.register_blueprint(visitor)
    app.register_blueprint(flat)
    app.register_blueprint(dashboard)


"""Create and return app."""
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SECURITY_PASSWORD_SALT'] = SECURITY_PASSWORD_SALT
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] =  os.environ['USERNAME']
app.config['MAIL_DEFAULT_SENDER'] = os.environ['USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASS']


mail = Mail(app)

CORS(app)
load_blueprints(app)

# db = PostgresqlDatabase(config.DATABASE_CONFIG['database'],
#                     user=config.DATABASE_CONFIG['user'],
#                     password=config.DATABASE_CONFIG['password'],
#                     host=config.DATABASE_CONFIG['host'],
#                     port=config.DATABASE_CONFIG['port'])