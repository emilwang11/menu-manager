import os
from image_repository import app, db
import unittest
import tempfile
import sqlite3 as sql

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['WTF_CSRF_ENABLED'] = False
        app.testing = True
        self.app = app.test_client()
        with app.app_context():
            db.initialize_db()
            #create temp in-memory test database
            # self.connection = sql.connect(self.db_fd)
            # cursor = self.connection.cursor()
            # cursor.execute("DROP TABLE IF EXISTS products")
            # cursor.execute("CREATE TABLE products (name TEXT, description TEXT, price FLOAT, stock INTEGER, imgpath TEXT)")
            # cursor.execute("""INSERT INTO products (name, description, price, stock, imgpath) VALUES \
            #     ('Penne Pasta', 'Our most popular dish...', 21.99, 10, '/static/images/pasta.jpeg'), \
            #     ('Chicken Noodle Soup', 'A heartwarming soup made with...', 9.99, 10, '/static/images/soup.jpeg'), \
            #     ('Strawberry Shortcake Cake', 'A delicious slice of cake...', 4.99, 10, '/static/images/cake.jpeg')
            # """)
            # cursor.execute("DROP TABLE IF EXISTS transactions")
            # cursor.execute("CREATE TABLE transactions (timestamp TEXT, productid INTEGER, value INTEGER)")
            # self.connection.commit()



    # def test_web_app_running(self):
    #     try:
    #         r = self.app.get("http://127.0.0.1:5000/")
    #     except:
    #         self.fail("Could not open web app. Not running, or crashed. Test Failed")

    #test routes load successfully
    def test_home_route(self):
        route = "/"
        rv = self.app.get(route)
        assert rv.status_code == 200


    def test_manage_route(self):
        route = "/manage"
        rv = self.app.get(route)
        assert rv.status_code == 200

    def test_edit_route(self):
        route = "/edit/1"
        rv = self.app.get(route)
        assert rv.status_code == 200

    #test functionality
    def test_buy(self):
        rv = self.app.get('/buy/1')
        assert b'Purchase successful!' in rv.data

    def test_edit(self):
        rv = self.app.post('/edit/1', data = dict(name="Pastaaa", price="10.2", stock="1"), follow_redirects=True)
        assert rv.status_code == 200
        assert b'Pastaaa' in rv.data

    def test_delete(self):
        rv = self.app.get('/delete/2')
        assert rv.status_code == 200
        assert b'Deletion successful!' in rv.data

    def test_total_earnings(self):
        rv = self.app.get('/manage')
        assert b'$21.99' in rv.data

    #tear down test database
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])


if __name__ == '__main__':
    unittest.main()
