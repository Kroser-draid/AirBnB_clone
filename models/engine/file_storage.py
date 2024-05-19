#!/usr/bin/python3
"""
Create filestorage class to manage data
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    class of filestorage that store data in json file and reload it
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        create new object in storage
        """
        obj_class_name = obj.__class__.__name__

        key = "{}.{}".format(obj_class_name, obj.id)

        FileStorage.__objects[key] = obj

    def all(self):
        """
        method that returns all objects in storage
        """
        return FileStorage.__objects

    def save(self):
        """
        method that saves the storage in the json file
        """
        all_objects = FileStorage.__objects

        object_dict = {}

        for obj in all_objects.keys():
            object_dict[obj] = all_objects[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        method that reload data from json file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    object_dict = json.load(f)

                    for key, value in object_dict.items():
                        class_name, object_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
