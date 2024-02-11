#!/usr/bin/python3
"""
Test script for FileStorage class.
"""

import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases."""

    def setUp(self):
        """The test environment."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Tear down the test environment."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test the all() method."""
        all_objects = FileStorage().all()
        self.assertEqual(all_objects, {})
        my_model = BaseModel()
        my_model.save()
        storage = FileStorage()
        storage.reload()
        all_objects = storage.all()
        self.assertIn("BaseModel." + my_model.id, all_objects)

    def test_new(self):
        """Test the new() method."""
        all_objects = FileStorage().all()
        self.assertEqual(all_objects, {})

        my_model = BaseModel()
        storage = FileStorage()
        storage.new(my_model)

        self.assertIn("BaseModel." + my_model.id, storage.all())

    def test_save(self):
        """Test the save() method."""
        self.assertFalse(os.path.exists("file.json"))

        my_model = BaseModel()
        my_model.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test the and reload() method."""
        self.assertFalse(os.path.exists("file.json"))

        storage = FileStorage()
        storage.reload()
        all_objects = storage.all()
        self.assertIn("BaseModel." + my_model.id, all_objects)

    def test_reload_nonexistent_file(self):
        """Test reload() with nonexistent file."""
        self.assertFalse(os.path.exists("file.json"))

        storage = FileStorage()
        storage.reload()
        all_objects = storage.all()
        self.assertEqual(all_objects, {})


if __name__ == "__main__":
    unittest.main()
