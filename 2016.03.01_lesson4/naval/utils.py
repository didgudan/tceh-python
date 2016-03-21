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


def make_coordinate_interval(start_coordinate, end_coordinate):
    x_interval = make_skipped_numbers(start_coordinate[0], end_coordinate[0])
    y_interval = make_skipped_numbers(start_coordinate[1], end_coordinate[1])

    if x_interval and y_interval:
        raise SyntaxError("Logic error! You can't have both X and Y coordinates increment!")

    if x_interval:
        return [[x_coord, start_coordinate[1]] for x_coord in x_interval]
    elif y_interval:
        return [[start_coordinate[0], y_coord] for y_coord in y_interval]