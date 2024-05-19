#!/usr/bin/python3
"""
Unit tests for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """

    def test_instance_creation(self):
        """
        Test if instance of BaseModel is created correctly
        """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_unique_id(self):
        """
        Test if each instance of BaseModel has a unique id
        """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_str_method(self):
        """
        Test the __str__ method of BaseModel
        """
        model = BaseModel()
        expected = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected)

    def test_save_method(self):
        """
        Test the save method of BaseModel
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict_method(self):
        """
        Test the to_dict method of BaseModel
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()
