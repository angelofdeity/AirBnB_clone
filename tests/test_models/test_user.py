#!/usr/bin/python3
"""Tests User class"""
import unittest
import pep8
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests for the User class"""

    @classmethod
    def setUpClass(cls):
        """Sets up test class"""
        cls.test_user = User()
        cls.test_user.email = "email"
        cls.test_user.password = "xxx"
        cls.test_user.first_name = "first"
        cls.test_user.last_name = "last"

    @classmethod
    def tearDownClass(cls):
        """Deletes test class"""
        del cls.test_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_conformance(self):
        """Tests pep8 conformance"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.\
            assertEqual(result.total_errors, 0, "Found style errors warnings.")

    def test_docstrings(self):
        """Tests docstrings"""
        self.assertGreater(len(User.__doc__), 0)
        for method in dir(User):
            if eval("User.{}.__doc__".format(method)) is not None:
                self.\
                    assertGreater(len(eval("User.{}.__doc__".format(method))), 0)

    def test_init_and_class_vars(self):
        """Tests __init__ and class variables"""
        self.assertIsInstance(self.test_user, User)
        self.assertIsInstance(self.test_user, BaseModel)
        self.assertIn('email', self.test_user.__dict__)
        self.assertIn('id', self.test_user.__dict__)
        self.assertIn('created_at', self.test_user.__dict__)
        self.assertIn('updated_at', self.test_user.__dict__)
        self.assertIn('password', self.test_user.__dict__)
        self.assertIn('first_name', self.test_user.__dict__)
        self.assertIn('last_name', self.test_user.__dict__)

    def test_save(self):
        """Tests the save method"""
        self.test_user.save()
        self.\
            assertNotEqual(self.test_user.created_at, self.test_user.updated_at)

    def test_str_types(self):
        """Tests the types of email, password, first_name, and last_name"""
        self.assertIsInstance(self.test_user.email, str)
        self.assertIsInstance(self.test_user.password, str)
        self.assertIsInstance(self.test_user.first_name, str)
        self.assertIsInstance(self.test_user.last_name, str)


if __name__ == '__main__':
    unittest.main()
