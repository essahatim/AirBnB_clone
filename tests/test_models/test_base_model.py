#!/usr/bin/python3
"""
The test script for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """The test cases."""

    def test_init(self):
        """Test instance attributes."""
        my_model = BaseModel()
        self.assertTrue(my_model.id)
        self.assertTrue(my_model.created_at)
        self.assertTrue(my_model.updated_at)

    def test_str(self):
        """Test _str_ method."""
        my_model = BaseModel()
        exp_str = (f"[BaseModel] ({my_model.id}) {my_model.__dict__}")
        self.assertTrue(str(my_model), exp_str)

    def test_save(self):
        """Test save method."""
        my_model = BaseModel()
        int_updated_at = my_model.updated_at
        my_model.save()
        new_updated_at = my_model.updated_at
        self.assertNotEqual(int_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        my_m_created =  my_model.created_at.isoformat()
        self.assertEqual(my_model_dict['created_at'], my_m_created)
        my_m_updated = my_model.updated_at.isoformat()
        self.assertEqual(my_model_dict['updated_at'], my_m_updated)

if __name__ == "__main__":
    unittest.main()

