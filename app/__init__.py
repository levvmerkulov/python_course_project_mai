from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy #ORM module
from flask_migrate import Migrate #DB migrations
from flask_login import LoginManager #Users logging in
from flask_mail import Mail

# initiate the Flask app
app_name = Flask(__name__)

# use config.py for configuration
app_name.config.from_object(Config)

# use Flask-Login for logging-in initialization
login = LoginManager(app_name)

# set an entrypoint for user
login.login_view = 'login'

# use SQLAlchemy for database management
db = SQLAlchemy(app_name)

# use flask_migrate for migration
migrate = Migrate(app_name, db)

# use Flask-Mail for email notification etc
mail = Mail(app_name)

from app import routes, models, errors