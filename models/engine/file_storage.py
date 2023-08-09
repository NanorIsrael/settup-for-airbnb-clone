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
        myKey = f"{obj.__class__}.{1}"
        FileStorage.__objects[myKey] = obj
        return FileStorage.__objects

    # def save(self):
    #     new_dict = {}
    #     for key, value in FileStorage.__objects.items():
    #         FileStorage.__objects[key] = value.to_dict()

    #         with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
    #             json.dump(new_dict, f)

    def reload(self):
        from models.base_model import BaseModel

        bnbClasses = {'BaseModel': BaseModel}
        try:
            with open(FileStorage.__file_path, "r") as f:
                content  = f.read()
                if content is None:
                    return
                temp = json.loads(content)

                for value in temp.values():
                    className = value["__class__"]
                    classObject = bnbClasses[className]
                    self.new(classObject(**value))

        except FileNotFoundError:
            pass
            

