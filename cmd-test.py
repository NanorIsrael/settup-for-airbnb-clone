import cmd


# class HelloWorld(cmd.Cmd):

#     def do_greet(self, person):
#         """greet [person]
#         Greet the named person"""
#         if person:
#             print("hi,", person)
#         else:
#             print('hi')

#     def do_EOF(self, line):
#         return True

#     def postloop(self):
#         print()

# if __name__ == '__main__':
#     HelloWorld().cmdloop()

class InteractiveOrCommandLine(cmd.Cmd):
    """Accepts commands via the normal interactive
    prompt or on the command line.
    """

    def do_greet(self, line):
        print('hello,', line)

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        InteractiveOrCommandLine().onecmd(' '.join(sys.argv[1:]))
    else:
        InteractiveOrCommandLine().cmdloop()