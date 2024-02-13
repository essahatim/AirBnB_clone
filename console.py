#!/usr/bin/python3
"""
Module containing the HBNBCommand class.
"""

import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Create a command interpreter with
    HBNBCommand class inherits from cmd.Cmd
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User"]

    def get_line(self):
        """Do an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        Saves it (to the JSON file), and prints the id
        Usage: create <class name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on:
            The class name
            The id
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in models.storage.all():
                print("** no instance found **")
                return
            else:
                print(models.storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on:
            The class name
            The id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in models.storage.all():
                print("** no instance found **")
                return
            else:
                del models.storage.all()[key]
                models.storage.save()

        def do_all(self, arg):
            """
            Prints all string representation of all instances
            Based or not on the class name.
            Usage: all [<class name>]
            """
            args = arg.split()
            if args and args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
            instance_list = []
            for key, value in models.storage.all().items():
                if not args or args[0] == key.split('.')[0]:
                    instance_list.append(str(value))
            if instance_list:
                print(instance_list)
            else:
                print("[]")

        def do_update(self, arg):
            """
            Updates an instance based on:
                The class name
                The id by adding or updating attribute
            Usage: update <class name> <id> <attribute name>
            """
            args = arg.split()
            if not args:
                print("** class name missing **")
            elif args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in models.storage.all():
                    print("** no instance found **")
                elif len(args) == 3:
                    print("** attribute value missing **")
                elif len(args) == 4:
                    print("** value missing **")
                else:
                    if args[4][0] == args[4][-1] == '"':
                        attribute_value = args[4][1:-1]
                    else:
                        attribute_value = args[4]
                    instance = models.storage.all()[key]
                    setattr(instance, args[2], attribute_value)
                    models.storage.all()[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
