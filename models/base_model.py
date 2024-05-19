#!/usr/bin/python3
"""
BaseModel module
Defines a BaseModel class for the AirBnB clone project.
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    A base class for all models that defines common attributes and methods.

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): The datetime when the instance is created.
        updated_at (datetime): The datetime when the instance is last updated.
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        
        Assigns a unique id and sets created_at and updated_at to the current datetime.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns the string representation of the instance.
        
        Format: [<class name>] (<self.id>) <self.__dict__>
        
        Returns:
            str: String representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        
        The dictionary contains all keys/values of __dict__ of the instance,
        with an additional key __class__ with the class name of the object.
        created_at and updated_at are converted to string in ISO format.
        
        Returns:
            dict: Dictionary representation of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
