# -*- coding: utf-8 -*-

__all__ = ('get_input_function', )


def get_input_function():
    try:
        input_function = raw_input
    except NameError:
        input_function = input

    return input_function


def make_skipped_numbers(start, end):
    max_number =  max(start, end)
    min_number =  min(start, end)

    if max_number == min_number:
        return False

    skipped_numbers = [min_number]
    while min_number < max_number:
        min_number += 1
        skipped_numbers.append(min_number)

    return skipped_numbers