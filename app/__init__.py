from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


# Initialize the app and the database
app = Flask(__name__)


db_path = os.path.join(os.path.dirname(__file__), 'kanban.db')
URI = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['DEBUG'] = True
# Set secret key for session management
app.config['SECRET_KEY'] = os.urandom(10)
db = SQLAlchemy(app)

from app import kanban_routing