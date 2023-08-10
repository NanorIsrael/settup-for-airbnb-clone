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
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
   
        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}
        try:
            loaded_json = {}
            with open(self.__file_path, 'r') as f:
                loaded_json = json.load(f)
                for key, val in loaded_json.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
