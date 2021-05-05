import sqlite3 as sql
from flask import Flask


app = Flask(__name__)

from image_repository import views, db

db.initialize_db()

