#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

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

    def do_create(self, args):
        """Creates a new instance
        """
        if len(args.split()) != 1:
            print("** class name missing **")

        elif args.split()[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        else:
            b = HBNBCommand.classes[args.split()[0]]()
            b.save()
            print(b.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and ID
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
        """Prints all string representation of all instances based or not on the class name
        """
        if args.split() and args.split()[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            for i in storage.all().values():
                print(str(i))

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
            setattr(_all[key], args.split()[2], args.split()[3])
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
