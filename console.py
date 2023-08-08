#!/usr/bin/env python3

import cmd

class InteractiveOrCommandLine(cmd.Cmd):
    prompt = '(hbnb) '
    doc_help = 'Documented commands (type help <topic>):'

    def do_prompt(self, line):
        print("({})".format(self.prompt))
    def do_help(self, line):
        print("\n\n{}".format(self.doc_help))
        print("=======================================")
        print('{}'.format(' '.join(['EOF', 'help', 'quit'])))
    def do_EOF(self, line):
        return True
    def do_quit(self, line):
        return True

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        InteractiveOrCommandLine().onecmd(''.join(sys.argv[1:]))
    else:
        InteractiveOrCommandLine().cmdloop()