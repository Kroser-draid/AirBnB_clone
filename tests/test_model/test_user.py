import os
import unittest
import models
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):


    def setUp(self):
        # create a temporary test file for saving data
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        # Remove the temporary test file after test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attributes(self):
        # create new user instance
        test_user = User()
        # check if the default email attribute is an empty string
        self.assertEqual(test_user.email, "")
        # Check if the default password attr is an empty string
        self.assertEqual(test_user.password, "")
        # Check if the default first_name attr is an empty string
        self.assertEqual(test_user.first_name, "")
        # Check if the default last_name is an empty string
        self.assertEqual(test_user.last_name, "")

    def test_user_inherits_from_base_model(self):
        # Create user instance
        test_user = User()
        # Check if the User class is a subclass of BaseModel
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_representation(self):
        # create new user instance
        test_user = User()
        # Set the attributes of the user instance
        test_user.email = "Ayoub@example.com"
        test_user.first_name = "Ayoub"
        test_user.last_name = "Kroser"
        test_user.password = "password123"
        # Get the string representation of the user instance
        user_str = str(test_user)
        # Check if "User" is present in the string representation
        self.assertIn("User", user_str)
        # Check if the email is present in the string representation
        self.assertIn("Ayoub@example.com", user_str)
        # Check if the first name is present in the string repr
        self.assertIn("Ayoub", user_str)
        # check if the last name present in the string repr
        self.assertIn("Kroser", user_str)

    def test_user_to_dict(self):
        # Create a new user instance
        test_user = User()
        # Set the attribute of the User instance
        test_user.email = "Ayoub@example.com"
        test_user.first_name = "Ayoub"
        test_user.last_name = "Kroser"
        test_user.save()
        # Get dictionary repre of the usr instance
        user_dict = test_user.to_dict()
        # check if the 'email' key in the dictionary matches the set value
        self.assertEqual(user_dict['email'], "Ayoub@example.com")
        # check the 'first_name' key in the dictionary matches the set value
        self.assertEqual(user_dict['first_name'], "Ayoub")
        # check the 'last_name' key in the dict matches the set value
        self.assertEqual(user_dict['last_name'], "Kroser")

    def test_user_instance_creation(self):
        # Create a new user instance with arguments
        test_user = User(email="Ayoub@example.com", password="password123", first_name="Ayoub", last_name="Kroser")
        # check if rhe "email" attribute is set correctly
        self.assertEqual(test_user.email, "Ayoub@example.com")
        # check if the password attr is set correctly
        self.assertEqual(test_user.password, "password123")
        # check if the "first_name" attr is set correctly
        self.assertEqual(test_user.first_name, "Ayoub")
        # check if the "last_name" attr is set correctly
        self.assertEqual(test_user.last_name, "Kroser")

    def test_user_instance_to_dict(self):
        # create a new user instance with specific attr values
        test_user = User(email="Ayoub@example.com", password="password123", first_name="Ayoub", last_name="Kroser")
        # convert the user instance to dict
        user_dict = test_user.to_dict()
        # check if the 'email' attribute is correctly represented in the dict
        self.assertEqual(user_dict['email'], "Ayoub@example.com")
        # check if the 'password' attribute is correctly represented in the dict
        self.assertEqual(user_dict['password'], "password123")
        # check if the 'first_name' attribute is correctly represented in the dict
        self.assertEqual(user_dict['first_name'], "Ayoub")
        # check if the 'last_name' attribute is correctly represented in the dict
        self.assertEqual(user_dict['last_name'], "Kroser")

    def test_user_id_generation(self):
        # Create two different user instances
        test_user = User()
        user2 = User()
        # ensure that the 'id' attr of each user is unique
        self.assertNotEqual(test_user.id, user2.id)


if __name__ == '__main__':
    unittest.main()
