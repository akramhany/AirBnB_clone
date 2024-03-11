#!/usr/bin/python3
""" Contains the main code of the command line interpreter """

import cmd
from models.base_model import BaseModel
from models.__init__ import storage


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
        Creates a new instance of class BaseModel, saves it and prints its id.
        """

        if not class_name:
            print("** class name missing **")
            return

        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return

        obj = BaseModel()
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
            if id == obj.id:
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

    def do_destroy(self, line):
        """ Takes the class name and id of an object and deletes it """

        if not self.is_valid(line):
            return

        argv = line.split(" ")
        id = argv[1]

        objects_list = storage.all()

        # loop over all of the stored objects, get the required obj with id.
        for key, obj in objects_list.items():
            if id == obj.id:
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
        if argv[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        elif len(argv) == 1:
            print("** instance id missing **")
            return False

        return True

    def emptyline(self):
        """ If an empty line is passed, do nothing """

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
