# -*- coding: utf-8 -*-

from __future__ import print_function

class Storage(object):
    obj = None
    items = None
    stage = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.stage = "data_input"
            cls.items = []
        return cls.obj


class Player(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return self.name


class Ship(object):
    def __init__(self, size, coordinates=[]):
        self.size = size
        self.coordinatesXY = coordinates

    def __str__(self):
        return self.coordinatesXY


class Field(object):
    def __init__(self, size=[10,10] ):
        self.shoots = []
        self.size = size

    # def __str__(self):
    #     return self.


# class Field(object):
#     def __init__(self):


# field1 = Field()

# p1 = Player("Alex")
# p1.own_field = Field()
# p1.opponent_field = Field()
# p1.own_field.ships = []
# print(p1)
#
# Storage().default_ships=[Ship(4), Ship(3), Ship(3), Ship(2), Ship(2)]

print(u'\u25A0\u25A0\u25A1', end="")
print("....x")
