#!/usr/bin/env python3
""" A class BaseModel that defines all common attributes/methods for other classes:
"""
from uuid import uuid4
from datetime import datetime
from sys import path
path.append('.')
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    att_value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, att_value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)
    
    def save(self):

        self.updated_at = datetime.now()
        # storage.save()

    def to_dict(self):
        dictionary = {}
        dictionary["__class__"] = self.__class__.__name__
        for key,value in self.__dict__.items():
            if isinstance(value, datetime):
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value

        return dictionary
    
    def __str__(self):
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))


print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

# storage = FileStorage()
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
save_instance = my_model.to_dict()
# print(save_instance)
data = storage.new(save_instance)
print(data)

