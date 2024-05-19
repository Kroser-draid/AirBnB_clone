#!/usr/bin/python3
"""
BaseModel class to inherite other classes from it
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    base model class
    """
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        models.storage.new(self)

    def save(self):
        """
        Method to save instance in storage
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Method that returns a dict of the instance
        """
        current_dict = self.__dict__.copy()
        current_dict["__class__"] = self.__class__.__name__
        current_dict["created_at"] = self.created_at.isoformat()
        current_dict["updated_at"] = self.updated_at.isoformat()

        return current_dict

    def __str__(self):
        """
        str method customized to return custom format of info
        """
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
