#!/usr/bin/python3
import os
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file
    Deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objs = {}
        for key, value in FileStorage.__objects.items():
            serialized_objs[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
            try:
                loaded_objs = json.load(file)
                for key, value in loaded_objs.items():
                    class_name, obj_id = key.split('.')
                    SomeClass = eval(class_name)
                    obj = SomeClass(**value)
                    FileStorage.__objects[key] = obj
            except FileNotFoundError:
                pass
