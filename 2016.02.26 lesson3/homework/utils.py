# -*- coding: utf-8 -*-


def get_input_function():
    try:
        input_function = raw_input
    except NameError:
        input_function = input

    return input_function
