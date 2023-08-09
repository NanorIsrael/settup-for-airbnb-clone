#!/usr/bin/python3
import json
from sys import path
path.append('.')

"""
a class FileStorage that serializes instances to a 
JSON file and deserializes JSON file to instances
"""


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """dictionary - empty but will store all objects by <class name>.id"""
        myKey = f"{obj.__class__.__name__}.{obj.id}" 
        self.__objects[myKey] = obj


    def save(self):
        """Stores the dict representation of instances in a file"""
        
        serialized_objects = {}
        
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as my_file:
            json_list = json.dumps(serialized_objects)
            my_file.write(json_list)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                content  = f.read()
                if content is None:
                    return
                json_from_file = json.loads(content)

                for key in json_from_file.keys():
                    created_instance = BaseModel(json_from_file[key])
                    deserialized_objects = {}
                    deserialized_objects = {**{key: created_instance}}
                return deserialized_objects
             
        except FileNotFoundError:
            pass
            