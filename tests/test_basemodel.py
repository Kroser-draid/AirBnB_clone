#!/user/bin/python3
import unittest
from models import BaseModel
from datetime import datetime
import time
import uuid


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up test case"""
        self.model = BaseModel()

    def test_id_is_uuid(self):
        """Test that id is a valid UUID"""
        self.assertIsInstance(uuid.UUID(self.model.id), uuid.UUID)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test that save() method updates updated_at"""
        old_updated_at = self.model.updated_at
        time.sleep(0.1)
        self.model.save()
        print("old_updated_at:", old_updated_at)
        print("new_updated_at:", self.model.updated_at)
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict() method"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['__class__'],
                         self.model.__class__.__name__)
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
