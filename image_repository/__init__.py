import sqlite3 as sql
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'f3cfe9ed8fae309f02079dbf' #exposed for dev and demo purposes only
csrf = CSRFProtect()
csrf.init_app(app)

from image_repository import views, db

db.initialize_db()

