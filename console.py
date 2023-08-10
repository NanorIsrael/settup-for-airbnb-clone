#!/usr/bin/env python3

import cmd
# from sys import path
# path.append('.')
from models.base_model import BaseModel
from models import FileStorage

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
        class_name = {"BaseModel": BaseModel}
        if not line:
            print("** class name missing **")
            return
        if class_name[line]:
            bm = class_name[line]()
            bm.save()
            print(bm.id)
        else:
            print("** class doesn't exist **")

    def  do_show(self, line):
        """Prints the string representation of an instance 
        based on the class name and id."""

        class_name = {"BaseModel": BaseModel}
        if not line:
            print("** class name missing **")
            return
        get_input = line.split(' ')
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

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(''.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()