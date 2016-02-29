# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import inspect
import pickle
import os.path
import glob

# import custom_exceptions
from custom_exceptions import UserExitException
from models import BaseItem
from utils import get_input_function

SAVE_PATH = "tasks"
SAVE_EXTENSION = ".task"


class BaseCommand(object):
    def __init__(self, command):
        self._command = command

    @property
    def command(self):
        return self._command

    @staticmethod
    def label():
        raise NotImplemented()

    def perform(self, objects, *args, **kwargs):
        raise NotImplemented()

    # list_ is a list needed to check index range in list
    def loop_input(self, list_=False):
        input_function = get_input_function()
        selection = None

        while True:
            try:
                selection = int(input_function('Input number: '))
                if list_:
                    list_[selection]
                break
            except (ValueError, IndexError):
                print('Bad input, try again.')

        return selection

    def check_objects_size(self, objects):
        if len(objects) == 0:
            print('There are no items in storage.')
            return False

        return True


class ListCommand(BaseCommand):
    @staticmethod
    def label():
        return 'list'

    def perform(self, objects, *args, **kwargs):
        if self.check_objects_size(objects) is False:
            return

        for index, obj in enumerate(objects):
            print('{}: {}, status is {}'.format(index, str(obj), obj.status))


class NewCommand(BaseCommand):
    @staticmethod
    def label():
        return 'new'

    @staticmethod
    def _load_item_classes():

        def class_filter(klass):
            return inspect.isclass(klass) \
                and klass.__module__ == BaseItem.__module__ \
                and issubclass(klass, BaseItem) \
                and klass is not BaseItem

        classes = inspect.getmembers(
            sys.modules[BaseItem.__module__],
            class_filter,
        )
        return dict(classes)

    def perform(self, objects, *args, **kwargs):
        classes = self._load_item_classes()

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print('{}: {}'.format(index, name))

        selection = self.loop_input(list(classes.keys()))

        selected_key = list(classes.keys())[selection]
        selected_class = classes[selected_key]
        print('Selected: {}'.format(selected_class.__name__))
        print()

        new_object = selected_class.construct()

        objects.append(new_object)
        print('Added {}'.format(str(new_object)))
        print()
        return new_object


class ExitCommand(BaseCommand):
    @staticmethod
    def label():
        return 'exit'

    def perform(self, objects, *args, **kwargs):
        raise UserExitException('See you next time!')


class DoneTypeCommand(BaseCommand):
    def perform(self, objects, current_status, *args, **kwargs):
        if self.check_objects_size(objects) is False:
            return

        print('Select item:')
        for index, obj in enumerate(objects):
            print('{}: {}'.format(index, str(obj)))

        selection = self.loop_input(objects)

        if objects[selection].status == current_status:
            print("It is already has status", str(current_status))
        else:
            objects[selection].status = current_status
            print('Status is set to:', objects[selection].status)


class DoneCommand(DoneTypeCommand):
    @staticmethod
    def label():
        return 'done'

    def perform(self, objects, *args, **kwargs):
        super(DoneCommand, self).perform(objects, "done", *args, **kwargs)


class UndoneCommand(DoneTypeCommand):
    @staticmethod
    def label():
        return 'undone'

    def perform(self, objects, *args, **kwargs):
        super(UndoneCommand, self).perform(objects, "undone", *args, **kwargs)


class SortCommand(BaseCommand):
    sort_order = ["by completeness", "by type"]

    @staticmethod
    def label():
        return 'sort'

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return

        print('Select sorting order:')
        for sort_type in self.sort_order:
            print('{}: {}'.format(self.sort_order.index(sort_type), sort_type))

        selection = self.loop_input(self.sort_order)

        if selection == 0:
            objects.sort(key=lambda obj: obj.status)
        elif selection == 1:
            objects.sort(key=lambda obj: obj.__class__.__name__)

        print("\nSorting result:")
        list_ = ListCommand("abc")
        list_.perform(objects)
        print()


class SaveCommand(BaseCommand):
    @staticmethod
    def label():
        return 'save'

    def perform(self, objects, *args, **kwargs):
        if self.check_objects_size(objects) is False:
            return

        input_function = get_input_function()

        while True:
            try:
                filename = input_function('Input filename to save data: ')
                filename = SAVE_PATH + "/" + filename + SAVE_EXTENSION

                if not os.path.exists(SAVE_PATH):
                    os.makedirs(SAVE_PATH)

                if os.path.isfile(filename):
                    while True:
                        print('File ', filename, 'already exist!')
                        answer = input_function('Rewrite (y/n)?')
                        if answer == "y":
                            break
                        if answer == "n":
                            return

                with open(filename, 'w') as outfile:
                    pickle.dump(objects, outfile, pickle.HIGHEST_PROTOCOL)
                break
            except IOError:
                print('Can\'t create such file!')

        print('All information was successfull dumped into', filename)


class LoadCommand(BaseCommand):
    @staticmethod
    def label():
        return 'load'

    def perform(self, objects, *args, **kwargs):
        input_function = get_input_function()

        if not os.path.exists(SAVE_PATH):
            print('There is load path!')
            return

        working_directory = os.getcwd()
        os.chdir(SAVE_PATH)
        print(glob.glob("*"))

        saved_files = glob.glob("*" + SAVE_EXTENSION)
        if len(saved_files) < 1:
            print('There is no files to load!')
            return

        while True:
            try:
                filename = input_function('Input filename to load data: ')
                if not os.path.isfile(filename):
                    raise SyntaxError
                with open(filename, 'rb') as infile:
                    loaded_objects = pickle.load(infile)
                break
            except SyntaxError:
                print('There is no such file!')

        for obj in loaded_objects:
            objects.append(obj)

        print('\nAll information was successfull loaded:')
        list_ = ListCommand("abc")
        list_.perform(objects)
        print()

        os.chdir(working_directory)
