#!/usr/bin/python3
from uuid import uuid4
import datetime
"""Module where the base classes are
"""


class BaseModel:
    """Base classe for other classes
    """

    def __init__(self):
        """initialize the instance attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """str method

        Returns:
            string: name of instance, id, and dict
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """method that update data
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """method that return dict

        Returns:
            str: isoformat of datetime of created and updated
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        if 'created_at' in result:
            result['created_at'] = result['created_at'].isoformat()
        if 'updated_at' in result:
            result['updated_at'] = result['updated_at'].isoformat()
        return result
