#!/usr/bin/python3
from uuid import uuid4
import datetime
"""Module where the base classes are
"""


class BaseModel:
    """_summary_
    """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[<{self.__class__.__name__}>] (<{self.id}>) <{self.__dict__}>"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        if 'created_at' in result:
            result['created_at'] = result['created_at'].isoformat()
        if 'updated_at' in result:
            result['updated_at'] = result['updated_at'].isoformat()
        return result
