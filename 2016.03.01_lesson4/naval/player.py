# -*- coding: utf-8 -*-

from __future__ import print_function

from utils import get_input_function, make_skipped_numbers, make_coordinate_interval
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

    def input_while_correct(self, message, type="ship"):
        input_function = get_input_function()

        while True:
            try:
                _input = input_function(message)
                self.check_coordinate_ethics(_input)
                _input = self.mutate_coordinates_to_digits(_input)
                if type == "ship":
                    self._check_coordinate_for_emptiness(_input)
                break
            except SyntaxError as msg:
                print(msg)

        return _input

    @staticmethod
    def _raise_error_if_wrong_ship_length(interval, ship_lenght):
        if interval:
            if len(interval) != ship_lenght:
                raise SyntaxError("Wrong ship length! You enter ship length " + str(len(interval)))

    def _check_coordinate_for_emptiness(self, coordinate):
        for ship in self.ships:
            if coordinate in ship.full_coordinates:
                raise SyntaxError("This cell already full of ships!")

    def _check_interval_for_emptiness(self, interval):
        for coordinate in interval:
            self._check_coordinate_for_emptiness(coordinate)

    def check_correct_ship_position(self, start_ship_coordinate, end_ship_coordinate, full_ship_coordinates, ship):
        if ship == 1 and (start_ship_coordinate == end_ship_coordinate):
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

        self._check_interval_for_emptiness(full_ship_coordinates)

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

    @staticmethod
    def make_full_ship_coordinates(start_ship_coordinate, end_ship_coordinate):
        # if we got 1 cell ship
        if start_ship_coordinate == end_ship_coordinate:
            return [start_ship_coordinate]

        return make_coordinate_interval(start_ship_coordinate, end_ship_coordinate)

    def place_ships(self, render_field):
        ships_by_rules = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        ships_by_rules = [4]

        for ship in ships_by_rules:
            render_field(self.field, self.ships)

            # while True:
            #     try:
            #         print(ship, "deck ship.")
            #         start_ship_coordinate = self.input_while_correct("Enter ship START coordinates (e.g. A4, B9, C5):")
            #         end_ship_coordinate = self.input_while_correct("Enter ship END coordinates (e.g. A4, B9, C5):")
            #         full_ship_coordinates = self.make_full_ship_coordinates(start_ship_coordinate, end_ship_coordinate)
            #
            #         self.check_correct_ship_position(
            #             start_ship_coordinate, end_ship_coordinate, full_ship_coordinates, ship
            #         )
            #         break
            #     except SyntaxError as msg:
            #         print(msg, "\n")
            #
            # new_ship = Ship(start_ship_coordinate, end_ship_coordinate, full_ship_coordinates)

            new_ship = Ship([0, 0], [0, 3], self.make_full_ship_coordinates([0, 0], [0, 3]))

            self.ships.append(new_ship)
            render_field(self.field, self.ships)

    def make_shot(self):
        shot_coordinate = self.input_while_correct("Make a shot (e.g. A4, B9, C5):", "shot")
        shot = Shot(shot_coordinate)
        self.shots.append(shot)
        return shot