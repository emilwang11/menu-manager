import sqlite3 as sql

from flask import Flask
from image_repository import views

app = Flask(__name__)

def initialize_db():
    connection = sql.connect("products.db")
    cursor = connection.cursor()

    #create table with products
    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.execute("CREATE TABLE products (name TEXT, description TEXT, price FLOAT, stock INTEGER, imgpath TEXT)")
    cursor.execute("""INSERT INTO products (name, description, price, stock, imgpath) VALUES \
        ('Pasta', 'This dish...', 19.99, 10, './static/images/pasta.jpeg'), \
        ('Soup', 'This dish...', 19.99, 10, './static/images/pasta.jpeg'), \
        ('Cake', 'This dish...', 19.99, 10, './static/images/pasta.jpeg')
    """)

    # Create empty transactions table
    cursor.execute("DROP TABLE IF EXISTS transactions")
    cursor.execute("CREATE TABLE transactions (timestamp TEXT, productid INTEGER, value INTEGER)")

    # Commit the db changes
    connection.commit()
    print("Initialized database")