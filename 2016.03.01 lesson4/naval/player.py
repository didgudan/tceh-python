# -*- coding: utf-8 -*-

from __future__ import print_function

from utils import get_input_function

from models import Ship
from consts import DICT


class Player(object):
    def __init__(self, name):
        self.name = name
        self.field = []
        self.ships = []
        self.shots = []

    def __str__(self):
        return self.name

    def input_while_correct(self, message):
        input_function = get_input_function()

        while True:
            try:
                input = input_function(message)
                self.check_coordinate_ethics(input)
                self.check_correct_ship_position(input)
                break
            except SyntaxError as msg:
                print(msg)

        return input

    def check_correct_ship_position(self, ship):
        pass

    @staticmethod
    def check_coordinate_ethics(coordinate):
        if (len(coordinate) < 2) and (len(coordinate) > 3):
            raise SyntaxError("There are must be 2 or 3 symbols in input!")
        if not coordinate[0].isalpha():
            raise SyntaxError("First symbol must be letter!")
        if not coordinate[1:].isdigit():
            raise SyntaxError("Second symbol must be digit!")
        if coordinate[0] not in DICT:
            raise SyntaxError("First coordinate must be on field!")
        if int(coordinate[1:]) not in DICT.values():
            raise SyntaxError("Second coordinate must be on field!")

    @staticmethod
    def mutate_cootdinates_to_digits(coordinates):
        return [
            int(DICT[
                    coordinates[0]
            ])-1,
            int(coordinates[1:]) - 1
        ]

    def place_ships(self, render_field):
        ships_by_rules = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

        for ship in ships_by_rules:
            render_field(self.field, self.ships)

            if len(self.ships) == 1: break

            print(ship, "deck ship.")
            start_ship_coordinate = self.input_while_correct("Enter ship START coordinates (e.g. A4, B9, C5):")
            end_ship_coordinate = self.input_while_correct("Enter ship END coordinates (e.g. A4, B9, C5):")

            # start_ship_coordinate = "A1"
            # end_ship_coordinate = "A9"

            new_ship = Ship(
                self.mutate_cootdinates_to_digits(start_ship_coordinate),
                self.mutate_cootdinates_to_digits(end_ship_coordinate)
            )
            print(new_ship.start_coordinate, new_ship.end_coordinate)

            self.ships.append(new_ship)


    def make_shot(self, shot):
        pass