#!/usr/bin/python3
""" Contains the main code of the command line interpreter """

import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.__init__ import storage
from models.__init__ import classes_list


class HBNBCommand(cmd.Cmd):
    """ The command line interpreter class """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """ When quit is typed, quits the cmd """

        return self.do_EOF(line)

    def do_EOF(self, line):
        """ Handles getting the EOF char """

        return True

    def do_create(self, class_name):
        """
        Creates a new instance of class name, saves it and prints its id.
        """

        if not class_name:
            print("** class name missing **")
            return

        name_exists = False
        for name in classes_list:
            if name == class_name:
                name_exists = True
                break

        if not name_exists:
            print("** class doesn't exist **")
            return

        # UPDATE when adding a new class.
        if class_name == "BaseModel":
            obj = BaseModel()
        elif class_name == "User":
            obj = User()
        elif class_name == "State":
            obj = State()
        elif class_name == "City":
            obj = City()
        elif class_name == "Amenity":
            obj = Amenity()
        elif class_name == "Place":
            obj = Place()
        elif class_name == "Review":
            obj = Review()

        obj.save()
        print(obj.id)

    def do_show(self, line):
        """ Print the string rep of an instance based on class name and id """

        if not self.is_valid(line):
            return

        argv = line.split(" ")
        id = argv[1]

        # loop over all of the stored objects, get the required obj with id.
        for obj in storage.all().values():
            if id == obj.id and argv[0] == obj.get_name():
                print(obj)
                return

        # if no obj with this id is found, print a message.
        print("** no instance found **")

    def do_all(self, line):
        """ Prints all string rep of all objs based or not on class name """

        objects_list = storage.all()
        str_list = []
        line = line.strip()
        for obj in objects_list.values():
            if not line:
                str_list.append(obj.__str__())
            else:
                if obj.get_name() == line:
                    str_list.append(obj.__str__())

        if len(str_list) == 0:
            print("** class doesn't exist **")
        else:
            print(str_list)

    def do_update(self, line):
        """
        Takes an argument name and a value, and set it for a certain obj id
        and a certain class name.
        """

        if not line:
            print("** class name missing **")
            return
        argv = line.split(" ")
        # hard coded check over class name, TODO: fix it.

        name_exists = False
        for name in classes_list:
            if name == argv[0]:
                name_exists = True
                break

        if not name_exists:
            print("** class doesn't exist **")
            return
        elif len(argv) == 1:
            print("** instance id missing **")
            return

        target = None
        for obj in storage.all().values():
            if obj.id == argv[1] and argv[0] == obj.get_name():
                target = obj
                break

        if target is None:
            print("** no instance found **")
            return

        if len(argv) == 2:
            print("** attribute name missing **")
            return
        elif len(argv) == 3:
            print("** value missing **")
            return

        attr_name, attr_value = argv[2], argv[3]
        attr_value = attr_value.strip('"\'')
        target.update(attr_name, attr_value)
        target.save()

    def do_destroy(self, line):
        """ Takes the class name and id of an object and deletes it """

        if not self.is_valid(line):
            return

        argv = line.split(" ")
        id = argv[1]

        objects_list = storage.all()

        # loop over all of the stored objects, get the required obj with id.
        for key, obj in objects_list.items():
            if id == obj.id and argv[0] == obj.get_name():
                del objects_list[key]
                storage.save()
                return

        # if no obj with this id is found, print a message.
        print("** no instance found **")

    # ------------------ TODO ------------------------
    # Handle class names doesn't exist errors.
    # ------------------------------------------------

    def is_valid(self, line):
        """ Takes an input string and makes sure its valid for commands """

        if not line:
            print("** class name missing **")
            return False

        argv = line.split(" ")

        name_exists = False
        for name in classes_list:
            if name == argv[0]:
                name_exists = True
                break

        if not name_exists:
            print("** class doesn't exist **")
            return
        elif len(argv) == 1:
            print("** instance id missing **")
            return False

        return True

    def emptyline(self):
        """ If an empty line is passed, do nothing """

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
