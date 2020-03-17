#coding=utf-8

import unittest
from author_book import db,Author,app
class DatabaseTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://liguang:123456@127.0.0.1:3306/liguang_flask_test'
        db.create_all()


    def test_add_author(self):
        author = Author(name="zhang",email="163@163.com")
        db.session.add(author)
        db.session.commit()

        result_author = Author.query.filter_by(name="zhang").first()
        self.assertIsNotNone(result_author)


    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
