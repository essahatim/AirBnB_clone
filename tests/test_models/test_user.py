#!/usr/bin/python3

import unittest
from models.user import User
import models
from models.base_model import BaseModel
import os


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up a clean environment before each test."""
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """Clean up the environment after each test."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_user_creation(self):
        """Test creating a new User instance."""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """Test User attributes."""
        user = User()
        user.email = "thm.ess@example.com"
        user.password = "123password"
        user.first_name = "thm"
        user.last_name = "ess"

        self.assertEqual(user.email, "thm.ess@example.com")
        self.assertEqual(user.password, "123password")
        self.assertEqual(user.first_name, "thm")
        self.assertEqual(user.last_name, "ess")

    def test_user_inherits_from_base_model(self):
        """Test if User inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attributes_default_values(self):
        """Test if User attributes have default values."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        
    def test_user_to_dict(self):
        """Test if to_dict method returns the expected dictionary."""
        user = User()
        user.email = "thm.ess@example.com"
        user.password = "123password"
        user.first_name = "thm"
        user.last_name = "ess"

        user_dict = user.to_dict()
        expected_keys = [
                'id', 'created_at', 'updated_at',
                'email', 'password', 'first_name',
                'last_name', '__class__'
                ]
        self.assertEqual(sorted(user_dict.keys()), sorted(expected_keys))

        for key in expected_keys:
            self.assertIn(key, user_dict)

        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "thm.ess@example.com")
        self.assertEqual(user_dict['password'], "123password")
        self.assertEqual(user_dict['first_name'], "thm")
        self.assertEqual(user_dict['last_name'], "ess")

    def test_user_str_representation(self):
        """Test if the string representation of User is as expected."""
        user = User()
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

    def test_user_save_reload(self):
        """Test saving and reloading a User instance."""
        user = User()
        user.email = "thm.ess@example.com"
        user.password = "123password"
        user.first_name = "thm"
        user.last_name = "ess"

        user.save()
        user_id = user.id

        models.storage.reload()
        reloaded_user = models.storage.all()["User.{}".format(user_id)]

        self.assertEqual(user.email, reloaded_user.email)
        self.assertEqual(user.password, reloaded_user.password)
        self.assertEqual(user.first_name, reloaded_user.first_name)
        self.assertEqual(user.last_name, reloaded_user.last_name)


if __name__ == "__main__":
    unittest.main()


