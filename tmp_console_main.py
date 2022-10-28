#!/usr/bin/python3
"""This module contains the class HBNBCommand"""


import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """This class that contains the entry point of the command interpreter"""
    prompt ='(hbnb) '
    clasess = {"BaseModel": BaseModel}

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

    def do_create(self,arg):
        """ Creates a new instance of BaseModel, saves it"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in self.clasess:
            print("** class doesn't exist **")
        else:
            new_obj = eval(arg)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in self.clasess:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_keys = args[0] + "." + args[1]
        all_objs = models.storage.all()

        for key, value in all_objs.items():
            if key == obj_keys:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if arg:
            arg = arg.split()
            if arg[0] not in self.clasess:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                compare = arg[0] + "." + arg[1]
                for key in models.storage.all().keys():
                    if key == compare:
                        del models.storage.all()[key]
                        models.storage.save()
                        return
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or
        not on the class name."""
        objs_list = []
        all_objs = models.storage.all()
        args = arg.split()

        if len(args) == 0:
            for key in all_objs:
                objs_list.append(all_objs[key].__str__())
            print(objs_list)
        elif args[0] in self.clasess:
            for key in all_objs:
                if all_objs[key].__class__.__name__ == args[0]:
                    objs_list.append(all_objs[key].__str__())
            print(objs_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3:
            print("** value missing **")
            return
        if arg[0] not in HBNBCommand.clasess:
            print("** class doesn't exist **")
            return
        all_objs = models.storage.all()
        for obj_id in all_objs.keys():
            if obj_id == arg[1]:
                setattr(all_objs[obj_id], arg[2], arg[3])
                models.storage.save()
                return
        print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
