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
