#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        myKey = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[myKey] = obj

    def save(self):
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            FileStorage.__objects[key] = value.to_dict()

            with open(FileStorage.__file_path, "w", encoding="uft-8") as f:
                json.dump(new_dict, f)

    def reload(self):
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
            

