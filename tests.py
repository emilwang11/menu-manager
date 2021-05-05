import os
from image_repository import app, db
import unittest
import tempfile
import sqlite3 as sql

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()
        #  with app.app_context():
        #     db.initialize_db()

        #create temp in-memory test database
        self.connection = sql.connect(":memory:")
        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS products")
        cursor.execute("CREATE TABLE products (name TEXT, description TEXT, price FLOAT, stock INTEGER, imgpath TEXT)")
        cursor.execute("""INSERT INTO products (name, description, price, stock, imgpath) VALUES \
            ('Penne Pasta', 'Our most popular dish...', 21.99, 10, '/static/images/pasta.jpeg'), \
            ('Chicken Noodle Soup', 'A heartwarming soup made with...', 9.99, 10, '/static/images/soup.jpeg'), \
            ('Strawberry Shortcake Cake', 'A delicious slice of cake...', 4.99, 10, '/static/images/cake.jpeg')
        """)
        cursor.execute("DROP TABLE IF EXISTS transactions")
        cursor.execute("CREATE TABLE transactions (timestamp TEXT, productid INTEGER, value INTEGER)")
        self.connection.commit()



    def test_web_app_running(self):
        try:
            r = self.app.get("http://127.0.0.1:5000/")
        except:
            self.fail("Could not open web app. Not running, or crashed. Test Failed")

    def test_buy(self):

        rv = self.app.post('/buy/1', follow_redirects=True)
        print(rv)
    #     #assert b'No entries here so far' not in rv.data

    def test_edit(self):

    def test_delete(self):

    def test_total_earnings(self):

    def tearDown(self):
        # os.close(self.db_fd)
        # os.unlink(app.config['DATABASE'])
        self.connection.close()

if __name__ == '__main__':
    unittest.main()
