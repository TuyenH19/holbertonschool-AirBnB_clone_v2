#!/usr/bin/python3
""" Module for testing db_storage"""
import unittest
from models import db_storage
from models.base_model import BaseModel
from models.user import User
from models.state import State


class TestDBStorage(unittest.TestCase):
    def setUp(self):
        self.db = db_storage.DBStorage()
        self.db.reload()

    def tearDown(self):
        self.db.close()

    def test_all(self):
        all_objects = self.db.all()
        self.assertIsInstance(all_objects, dict)

        users = self.db.all(User)
        self.assertIsInstance(users, dict)

        states = self.db.all(State)
        self.assertIsInstance(states, dict)

    def test_new_save_delete(self):
        new_user = User()
        new_user.name = "John Doe"
        new_user.email = "john@example.com"
        self.db.new(new_user)
        self.db.save()

        all_users = self.db.all(User)
        self.assertIn(new_user.id, all_users)

        self.db.delete(new_user)
        self.db.save()

        all_users = self.db.all(User)
        self.assertNotIn(new_user.id, all_users)


if __name__ == '__main__':
    unittest.main()
