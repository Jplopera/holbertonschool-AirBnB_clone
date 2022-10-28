#!/usr/bin/python3
"""This module contains the class HBNBCommand"""


import cmd


class HBNBCommand(cmd.Cmd):
    """This class that contains the entry point of the command interpreter"""
    prompt ='(hbnb) '

    def do_quit(self, arg):
        """Quit command"""
        quit()
        return True

    def do_EOF(self, line):
        """Closes the program"""
        return True

    def emptyline(self):
        """doesn't execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
