#!/usr/bin/python3
"""
Module containing the BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """ Base class for all models"""

    def __init__(self):
        """Initialize the instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the instance."""
        ClassName = self.__class__.__name__
        return (f"[{ClassName}] ({self.id}) {self.__dict__}")

    def save(self):
        """Update the public instance with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__.
        A key __class__ is added ,with the class name of the object.
        The instanc are converted to string objects in ISO format.
        """
        result_dict = self.__dict__.copy()
        result_dict["__class__"] = self.__class__.__name__
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        return result_dict


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(
            key, type(my_model_json[key]), my_model_json[key]
            ))
