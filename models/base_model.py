#!/usr/bin/env python3
""" A class BaseModel that defines all common attributes/methods for other classes:
"""

from uuid import uuid4
from datetime import datetime


class Base:
    def __init__(self):
        """method to instantiate an instance"""
        self.id = str(uuid4())
        self.created_at =  datetime.now().isoformat()
    def __str__(self):
        """method to create a string copy an instance attributes"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    def save(self):
        """Defines the update of a Base"""
        self.updated_at =  datetime.now().isoformat()
    def to_dict(self):
        """Defines a method that returns a dictionary of an instance attr"""
        return self.__dict__
    
base = Base()
# help(Base)
print(base)
print(base.id)
print(base.created_at)