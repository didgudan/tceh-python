# -*- coding: utf-8 -*-

from __future__ import print_function


class Ship(object):
    def __init__(self, start_coordinate, end_coordinate):
        self.start_coordinate = start_coordinate
        self.end_coordinate = end_coordinate

    def __str__(self):
        return str(self.start_coordinate) + "-" + str(self.end_coordinate)


class Field(object):
    def __init__(self, size=10):
        if (size > 99) or (size < 5):
            raise IndexError("Size of game filed must be between 5 and 99 squares!")

        self.shoots = []
        self.size = size

    # def __str__(self):
    #     return self.


class Shot(object):
    def __init__(self, coordintate):
        self.coordinate = coordintate

    def __str__(self):
        return self.coordinate


# print(u'\u25A0\u25A0\u25A1', end="")
# print("....x")
