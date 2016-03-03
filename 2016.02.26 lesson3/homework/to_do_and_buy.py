# -*- coding: utf-8 -*-

from __future__ import print_function

import inspect
import sys

from commands import (
    BaseCommand,
    DoneTypeCommand,

    UserExitException,
)
from models import (
    Storage,
)
from utils import *

__author__ = 'sobolevn'


def get_routes():
    def class_filter(klass):
        return inspect.isclass(klass) \
            and klass.__module__ == BaseCommand.__module__ \
            and issubclass(klass, BaseCommand) \
            and klass is not BaseCommand \
            and klass is not DoneTypeCommand

    routes = inspect.getmembers(
        sys.modules[BaseCommand.__module__],
        class_filter
    )
    return dict((route.label(), route) for _, route in routes)


def perform_command(command):
    command = command.lower()
    routes = get_routes()

    try:
        command_class = routes[command]
        command_inst = command_class(command)

        storage = Storage()
        command_inst.perform(storage.items)
    except KeyError:
        print('Bad command, try again.')
    except UserExitException as ex:
        print(ex)
        raise


def parse_user_input():
    input_function = get_input_function()

    message = 'Input your command: (%s): ' % '|'.join(
        get_routes().keys())
    return input_function(message)


def main():
    while True:
        try:
            command = parse_user_input()
            perform_command(command)
        except UserExitException:
            break
        except KeyboardInterrupt:
            print('Shutting down, bye!')
            break


if __name__ == '__main__':
    # main()

    class Storage(object):
        obj = None

        items = None

        @classmethod
        def __new__(cls, *args):
            if cls.obj is None:
                cls.obj = object.__new__(cls)
                cls.items = []
            return cls.obj

    s1 = Storage()
    s1.items.append(1)

    s2 = Storage()
    s2.items.append(2)

    print(s1.items)
    print(s2.items)