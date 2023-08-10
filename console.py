#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import FileStorage
import uuid
import re

"""Defines a console app for airbnb application"""


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    doc_help = 'Documented commands (type help <topic>):'
    doc_header = 'Documented commands (type help <topic>):'

    def do_prompt(self, line):
        """Provides a cli prompt to interact with the program"""
        print("({})".format(self.prompt))
   
    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    def emptyline(self):
        """Do nothing on an empty line"""
        pass
    
    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for EOF command"""
        print("Exit the program with EOF (Ctrl-D)")

    def  do_create(self, line):
        """Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id"""
        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}
        if not line:
            print("** class name missing **")
            return
        if classes[line]:
            bm = classes[line]()
            bm.save()
            print(bm.id)
        else:
            print("** class doesn't exist **")

    def  do_show(self, line):
        """Prints the string representation of an instance 
        based on the class name and id."""

        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}

        if not line:
            print("** class name missing **")
            return
        get_input = line.split(' ')
        if not get_input[0] in classes:
            print("** class doesn't exist **")
            return
        if len(get_input) <= 1:
            print("** instance id missing **")
            return
        
        search_key = f"{get_input[0]}.{get_input[1]}"
        db = FileStorage()
        db.reload()
        result = db.all()
        if search_key in result:
            print(result[search_key])
        else:
            print(f"** no instance found **")

    def  do_destroy(self, line):
        """Deletes an instance based on the class name and
        id (save the change into the JSON file). """

        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}
        if not line:
            print("** class name missing **")
            return
        get_input = line.split(' ')
        if not get_input[0] in classes:
            print("** class doesn't exist **")
            return
        if len(get_input) <= 1:
            print("** instance id missing **")
            return
        search_key = f"{get_input[0]}.{get_input[1]}"
        db = FileStorage()
        db.reload()
        result = db.all()
        if search_key in result:
            del result[search_key]
            db.save()
        else:
            print(f"** no instance found **")

    def  do_all(self, line):
        """Deletes an instance based on the class name and
        id (save the change into the JSON file). """

        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}
        db = FileStorage()
        db.reload()
        result = db.all()
        if line:
                if not line in classes:
                    print("** class doesn't exist **")
                    return
                else:
                    all_models = []
                    for key, value in result.items():
                        key_class = key.split('.')
                        if key_class[0] == line:
                            all_models.append(str(value))
                    print(all_models) 
        else:
            if result:
                all_models = []
                for key, value in result.items():
                    all_models.append(str(result[key]))
                print(all_models) 
            else:
                print("** no instance found **")

    def  do_update(self, line):
        """Updates an instance based on the class name and id
         by adding or updating attribute (save the change into 
         the JSON file)."""
        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}
        if not line:
            print("** class name missing **")
            return
        else:
            params = line.split(' ')
            class_name = params[0]            
            if not class_name in classes:
                print("** class doesn't exist **")
                return
            if len(params) < 2:
                print("** instance id missing **")
                return
            id_value = params[1]
            db = FileStorage()
            db.reload()
            found = False
            found_instance = []
            for key, value in db.all().items():
                if id_value == value.id:
                    found_instance.append(value)
                    found = True
            if not found:
                print("** no instance found **")
                return
            if len(params) < 3:
                print("** attribute name missing **")
                return
            if len(params) < 4:
                print("** value missing **")
                return
            else:
                attr_name = params[2]
                attr_value = params[3].strip('"')
                if attr_name in ['id, created_at, updated_at']:
                    pass
                else:
                    instance = found_instance[0]
                    attr_name = attr_name.replace('"', '')
                    original_attr = getattr(instance, attr_name, None)
                    if not original_attr is None:
                        attr_type = type(original_attr) 
                        casted_attr_value = attr_type(attr_value)
                        setattr(instance, attr_name, casted_attr_value)
                    else:
                        if attr_value[0] == '\"':
                            attr_value = attr_value.replace('"', '')
                        else:
                            pattern = re.compile(r'^[-+]?[0-9]*\.[0-9]+([eE][-+]?[0-9]+)?$')
                            match = re.match(pattern, attr_value)
                            if match:
                                attr_value = float(attr_value)
                            else:
                                attr_value = int(attr_value)
                        setattr(instance, attr_name, attr_value)
                    print(instance)
                    instance.save()
# 5.5
    def default(self, line):
        """Handle custom commands"""
        parts = line.partition('.')
        if len(parts) == 3:
            class_name = parts[0]
            classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}
            db = FileStorage()
            db.reload()
            result = db.all()
            
            if not class_name in classes:
                print("** class doesn't exist **")
                return
            else:
                all_models = [value for key, value in result.items() if key.startswith(f"{class_name}.")]
                formatted_models = ', '.join(map(str, all_models))
                if parts[2] == "all()":
                    print(f"[{formatted_models}]")
                if parts[2] == "count()":
                    print(len(all_models))

                pattern = re.compile(r'^show\((.*)\)$', re.IGNORECASE)
                match = pattern.match(parts[2])
                if match:
                    match = pattern.match(parts[2])
                    id_value = match.group(2).strip('"')
                    search_string = f"{class_name} {id_value}"
                    self.do_show(f"{class_name} {id_value}")
            
                pattern = re.compile(r'^destroy\((.*)\)$', re.IGNORECASE)
                match = pattern.match(parts[2])
                if match:
                    match = pattern.match(parts[1])
                    id_value = match.group(1).strip('"')
                    search_string = f"{class_name} {id_value}"
                    self.do_destroy(f"{class_name} {id_value}")
                
                pattern = re.compile(r'^update\((.*)\)$', re.IGNORECASE)
                match = pattern.match(parts[2])
                if match:
                    params = match.group(1)
                    # Split the parameters by commas
                    splitted_params = [param.strip('"') for param in params.split(',')]
                    if len(splitted_params) >= 3:
                        id_value, attr_name, attr_value = splitted_params[:3]
                        attr_name = attr_name.replace(" ", "")
                        attr_value = attr_value.replace(" ", "")
                        update_string = f"{class_name} {id_value} {attr_name} {attr_value}"
                        self.do_update(update_string)


if __name__ == '__main__':
    import sys
    if sys.stdin.isatty():
        HBNBCommand().cmdloop()
    else:
        input_data = sys.stdin.read().strip()
        cmd_instance = HBNBCommand()
        cmd_instance.onecmd(input_data)

