#!/usr/bin/python3
import json
from sys import path
path.append('.')

"""
a class FileStorage that serializes instances to a 
JSON file and deserializes JSON file to instances
"""


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """dictionary - empty but will store all objects by <class name>.id"""
        myKey = f"{obj['__class__']}.{obj['id']}"
        FileStorage.__objects[myKey] = obj
        return FileStorage.__objects

    def save(self):
        """Stores the dict representation of an instance in a file"""
        with open(self.__file_path, 'w') as my_file:
            json_list = json.dumps(self.__objects)
            my_file.write(json_list)

    # def reload(self):
    #     from models.base_model import BaseModel

    #     bnbClasses = {'BaseModel': BaseModel}
    #     try:
    #         with open(FileStorage.__file_path, "r") as f:
    #             content  = f.read()
    #             if content is None:
    #                 return
    #             temp = json.loads(content)

    #             for value in temp.values():
    #                 className = value["__class__"]
    #                 classObject = bnbClasses[className]
    #                 self.new(classObject(**value))

    #     except FileNotFoundError:
    #         pass
            

