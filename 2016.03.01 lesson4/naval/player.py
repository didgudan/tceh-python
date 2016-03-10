# -*- coding: utf-8 -*-

from __future__ import print_function

from utils import get_input_function, make_skipped_numbers
from models import Ship, Shot
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
                _input = input_function(message)
                self.check_coordinate_ethics(_input)
                break
            except SyntaxError as msg:
                print(msg)

        return _input

    @staticmethod
    def _raise_error_if_wrong_ship_length(interval, ship_lenght):
        if interval:
            if len(interval) != ship_lenght:
                raise SyntaxError("Wrong ship length! You enter ship length " + str(len(interval)))

    def check_correct_ship_position(self, start_ship_coordinate, end_ship_coordinate, ship):
        if ship == 1:
            return

        if start_ship_coordinate == end_ship_coordinate:
            raise SyntaxError("Baby! Coordinates can't be same!")

        if (start_ship_coordinate[0] != end_ship_coordinate[0]) and \
           (start_ship_coordinate[1] != end_ship_coordinate[1]):
            raise SyntaxError("Ship must be straight line!")

        for ind in range(2):
            self._raise_error_if_wrong_ship_length(
                make_skipped_numbers(start_ship_coordinate[ind], end_ship_coordinate[ind]),
                ship
            )

    @staticmethod
    def check_coordinate_ethics(coordinate):
        if (len(coordinate) < 2) and (len(coordinate) > 3):
            raise SyntaxError("There are must be 2 or 3 symbols in input!")
        if not coordinate[0].isalpha():
            raise SyntaxError("First symbol must be letter!")
        if not coordinate[1:].isdigit():
            raise SyntaxError("Second symbol must be digit!")
        if coordinate[0] not in DICT or int(coordinate[1:]) not in DICT.values():
            raise SyntaxError("Both coordinates must be on field!")

    @staticmethod
    def mutate_coordinates_to_digits(coordinates):
        return [
            int(DICT[
                    coordinates[0]
            ])-1,
            int(coordinates[1:]) - 1
        ]

    def place_ships(self, render_field):
        ships_by_rules = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        ships_by_rules = [1]

        for ship in ships_by_rules:
            render_field(self.field, self.ships)

            # while True:
            #     try:
            #         print(ship, "deck ship.")
            #         start_ship_coordinate = self.input_while_correct("Enter ship START coordinates (e.g. A4, B9, C5):")
            #         end_ship_coordinate = self.input_while_correct("Enter ship END coordinates (e.g. A4, B9, C5):")
            #
            #         start_ship_list_coordinate = self.mutate_coordinates_to_digits(start_ship_coordinate)
            #         end_ship_list_coordinate = self.mutate_coordinates_to_digits(end_ship_coordinate)
            #
            #         self.check_correct_ship_position(start_ship_list_coordinate, end_ship_list_coordinate, ship)
            #         break
            #     except SyntaxError as msg:
            #         print(msg, "\n")
            #
            # new_ship = Ship(start_ship_list_coordinate, end_ship_list_coordinate)
            new_ship = Ship([0, 0], [0, 0])

            self.ships.append(new_ship)

            render_field(self.field, self.ships)

    def make_shot(self):
        shot_coordinate = self.input_while_correct("Make a shot (e.g. A4, B9, C5):")
        shot_list_coordinate = self.mutate_coordinates_to_digits(shot_coordinate)

        shot = Shot(shot_list_coordinate)
        self.shots.append(shot)