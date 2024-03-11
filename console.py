#!/usr/bin/python3
""" Contains the main code of the command line interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """ The command line interpreter class """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """ When quit is typed, quits the cmd """

        return self.do_EOF(line)

    def do_EOF(self, line):
        """ Handles getting the EOF char """

        return True

    def emptyline(self):
        """ If an empty line is passed, do nothing """

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
