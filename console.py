#!/usr/bin/python3
"""[HBNBCommand class]
"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """[HBNBCommand class]

    Args:
        cmd ([module]): [cmd module for command prompt]

    Returns:
        [bool]: [true or false]
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel,
               "User": User,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Place": Place,
               "Review": Review}

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """[empty line]
        """
        pass

    def default(self, line):
        """[default method]

        Args:
            line ([str]): [user's input]

        Returns:
            [function]: [returns the function needed or error]
        """
        lst = line.replace('(', '.')[:-1].split('.')
        if len(lst) > 1:
            if lst[1] == "all":
                return self.do_all(lst[0])

            elif lst[1] == "show":
                return self.do_show(lst[0] + ' ' + lst[2])

            elif lst[1] == "destroy":
                return self.do_destroy(lst[0] + ' ' + lst[2])

            elif lst[1] == "update":
                return self.do_update(lst[0] + ' ' + lst[2])

            elif lst[1] == "count":
                print(len(storage.all()))

    def do_create(self, args):
        """Creates a new instance
        """
        args = args.split()
        if not args:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        else:
            b = HBNBCommand.classes[args[0]]()
            b.save()
            print(b.id)

    def do_show(self, args):
        """Prints the string representation of an \
            instance based on the class name and ID
        """
        arg = args.split()
        _all = storage.all()
        if not arg:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        else:
            print(_all["{}.{}".format(args.split()[0], args.split()[1])])

    def do_destroy(self, args):
        """Destroy By ID
        """
        _all = storage.all()
        if len(args.split()) == 0:
            print("** class name missing **")

        elif args.split()[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        else:
            del _all["{}.{}".format(args.split()[0], args.split()[1])]
            storage.save()

    def do_all(self, args):
        """Prints all string representation of \
            all instances based or not on the class name
        """
        args = args.split()
        lst = []
        if args and args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif not args:
            for i in storage.all().values():
                lst.append(str(i))
        else:
            for i in storage.all().values():
                if args[0] == i.__class__.__name__:
                    lst.append(str(i))
        if len(lst):
            print(lst)

    def do_update(self, args):
        _all = storage.all()
        key = "{}.{}".format(args.split()[0], args.split()[1])
        if len(args.split()) == 0:
            print("** class name missing **")

        elif args.split()[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        elif len(args.split()) == 2:
            print("** attribute name missing **")

        elif len(args.split()) == 3:
            print("** value missing **")
        else:
            setattr(_all[key], args.split()[2], re.search(r'\w+', args.split()[3]).group())
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
