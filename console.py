#!/usr/bin/env python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    doc_help = 'Documented commands (type help <topic>):'

    def do_prompt(self, line):
        print("({})".format(self.prompt))
    def do_help(self, line):
        print("\n\n{}".format(self.doc_help))
        print("=======================================")
        print('{}\n'.format(' '.join(['EOF', 'help', 'quit'])))
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


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(''.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()