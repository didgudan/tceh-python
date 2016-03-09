# -*- coding: utf-8 -*-

import collections
import string

__all__ = ('get_input_function', )




DICT = {char: string.ascii_uppercase.index(char)+1 for char in string.ascii_uppercase[0:def_size]}
DICT = collections.OrderedDict(sorted(DICT.items(), key=lambda t: t[0]))


def get_input_function():
    try:
        input_function = raw_input
    except NameError:
        input_function = input

    return input_function