#!/usr/bin/python3
"""

"""
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    def test_init(self):
        my = BaseModel()

        self.assertIsNotNone(my.id)
        self.assertIsNotNone(my.created_at)
        self.assertIsNotNone(my.updated_at)

    def test_save(self):
        my = BaseModel()

        init_updated_at = my.updated_at
        current_updated_at = my.save()
        self.assertNotEqual(init_updated_at, current_updated_at)

    def test_to_dict(self):
        my = BaseModel()

        my_dict = my.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertEqual(my_dict["__class__"], "BaseModel")
        self.assertEqual(my_dict["id"], my.id)
        self.assertEqual(my_dict["created_at"], my.created_at.isoformat())
        self.assertEqual(my_dict["updated_at"], my.updated_at.isoformat())

    def test_str(self):
        my = BaseModel()

        self.assertTrue(str(my).startswith('[BaseModel]'))
        self.assertIn(my.id, str(my))
        self.assertIn(str(my.__dict__), str(my))


if __name__ == "__main__":
    unittest.main()
