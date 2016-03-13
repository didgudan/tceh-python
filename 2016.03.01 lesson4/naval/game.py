# -*- coding: utf-8 -*-

from __future__ import print_function

from models import Field, Shot, Ship, Player
from utils import get_input_function
from consts import DICT, EMPTY_MARK, SHIP_MARK, MISS_SHOT, HIT_SHOT


# singleton
class Game(object):
    obj = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
        return cls.obj

    def __init__(self):
        self.stage = "data_input"
        self.turn = 0
        self.active_player = None
        self.not_active_player = None

    def make_shot(self):
        shot_coordinate = self.input_while_correct(
            "Make a shot (e.g. A4, B9, C5):", "shot")
        shot = Shot(shot_coordinate)
        self.active_player.shots.append(shot)
        return shot

    @staticmethod
    def check_coordinate_ethics(coordinate):
        if (len(coordinate) < 2) and (len(coordinate) > 3):
            raise SyntaxError("There are must be 2 or 3 symbols in input!")
        if not coordinate[0].isalpha():
            raise SyntaxError("First symbol must be letter!")
        if not coordinate[1:].isdigit():
            raise SyntaxError("Second symbol must be digit!")
        if (coordinate[0] not in DICT) or \
           (int(coordinate[1:]) not in DICT.values()):
            raise SyntaxError("Both coordinates must be on field!")

    @staticmethod
    def mutate_coordinates_to_digits(coordinates):
        return [
            int(DICT[coordinates[0]])-1,
            int(coordinates[1:]) - 1
        ]

    @staticmethod
    def make_skipped_numbers(start, end):
        max_number = max(start, end)
        min_number = min(start, end)

        if max_number == min_number:
            return False

        skipped_numbers = [min_number]
        while min_number < max_number:
            min_number += 1
            skipped_numbers.append(min_number)

        return skipped_numbers

    def make_coordinate_interval(self, start_coordinate, end_coordinate):
        x_interval = self.make_skipped_numbers(start_coordinate[0],
                                               end_coordinate[0])
        y_interval = self.make_skipped_numbers(start_coordinate[1],
                                               end_coordinate[1])

        if x_interval and y_interval:
            raise SyntaxError("Logic error! You can't have"
                              " both X and Y coordinates increment!")

        if x_interval:
            return [[x_coord, start_coordinate[1]] for x_coord in x_interval]
        elif y_interval:
            return [[start_coordinate[0], y_coord] for y_coord in y_interval]

    def _check_coordinate_for_emptiness(self, coordinate):
        for ship in self.active_player.ships:
            if coordinate in ship.full_coordinates:
                raise SyntaxError("Some cell already full of ships!")

    def check_correct_ship_position(
            self, start_ship_coordinate, end_ship_coordinate,
            full_ship_coordinates, ship):
        if ship == 1 and (start_ship_coordinate == end_ship_coordinate):
            return True

        if start_ship_coordinate == end_ship_coordinate:
            raise SyntaxError("Baby! Coordinates can't be same!")

        if (start_ship_coordinate[0] != end_ship_coordinate[0]) and \
           (start_ship_coordinate[1] != end_ship_coordinate[1]):
            raise SyntaxError("Ship must be straight line!")

        for ind in range(2):
            self._raise_error_if_wrong_ship_length(
                self.make_skipped_numbers(
                    start_ship_coordinate[ind],
                    end_ship_coordinate[ind]), ship
            )

        self._check_interval_for_emptiness(full_ship_coordinates)

    def _check_interval_for_emptiness(self, interval):
        for coordinate in interval:
            self._check_coordinate_for_emptiness(coordinate)

    @staticmethod
    def _raise_error_if_wrong_ship_length(interval, ship_lenght):
        if interval:
            if len(interval) != ship_lenght:
                raise SyntaxError("Wrong ship length! You enter ship length " +
                                  str(len(interval)))

    def input_while_correct(self, message, _type="ship"):
        input_function = get_input_function()

        while True:
            try:
                _input = input_function(message)
                _input = _input.upper()
                self.check_coordinate_ethics(_input)
                _input = self.mutate_coordinates_to_digits(_input)
                if _type == "ship":
                    self._check_coordinate_for_emptiness(_input)
                break
            except SyntaxError as msg:
                print(msg)

        return _input

    def _check_player_name_identity(self, second_player_name):
        if not self.active_player:
            return

        if self.active_player.name == second_player_name:
            raise SyntaxError("Players name can't be same!")

    def change_players(self):
        self.active_player, self.not_active_player = \
            self.not_active_player, self.active_player

    def activate_player(self):
        while True:
            try:
                name = input_function('\nInput player name: ')
                self._check_player_name_identity(name)
                break
            except SyntaxError as msg:
                print(msg)

        # name = "Alex"
        # if self.active_player:
        #     name = "Alex_clone"

        if self.active_player:
            self.change_players()

        self.active_player = Player(name)
        print(self.active_player, "turn")

    def render_field(self, **kwargs):
        if kwargs['field_type']:
            print(kwargs['field_type'], "field:\n")

        rendered_field = []

        # render field
        for x in range(kwargs['field'].size[0]):
            rendered_field.append([])
            for y in range(kwargs['field'].size[1]):
                rendered_field[x].append(EMPTY_MARK)

        # render ships
        if kwargs['ships']:
            for ship in kwargs['ships']:
                for coordinate in ship.full_coordinates:
                    rendered_field[coordinate[1]][coordinate[0]] = SHIP_MARK

        # render shots
        if kwargs['shots']:
            for shot in kwargs['shots']:
                # if we render opposite filed
                if kwargs['opposite_ships']:
                    if self.check_ship_presence_for_cell(
                            shot.coordinate, kwargs['opposite_ships']
                    ):
                        rendered_field[shot.coordinate[1]][
                            shot.coordinate[0]] = HIT_SHOT
                        continue
                # if we render own filed
                else:
                    if rendered_field[shot.coordinate[1]][
                        shot.coordinate[0]
                    ] == SHIP_MARK:
                        rendered_field[shot.coordinate[1]][
                            shot.coordinate[0]] = HIT_SHOT
                        continue

                rendered_field[shot.coordinate[1]][
                    shot.coordinate[0]] = MISS_SHOT

        # add all keys in DICT as first list in render_field
        rendered_field.insert(0, list(DICT.keys()))
        rendered_field[0].insert(0, "  ")

        num = 1
        for lst in rendered_field[1:]:
            lst.insert(0, "{:>{w}}".format(num, w=2))
            num += 1

        # print render_field
        for string in rendered_field:
            for elem in string:
                print(elem, end="")
            print()
        print()

    @staticmethod
    def check_ship_presence_for_cell(cell_coordinates, ships):
        for ship in ships:
            if cell_coordinates in ship.full_coordinates:
                return ship

        return False

    def mark_ship_as_destroyed(self, ship):
        for current_ship_coordinate in ship.full_coordinates:
            if not self._check_shot_coordinate_presence(
                    current_ship_coordinate, self.active_player.shots
            ):
                return False

        self.add_surround_shots(ship)
        ship.padded = True
        return True

    @staticmethod
    def _check_shot_coordinate_presence(shot_coordinate, shots):
        list_of_all_shots = [sh.coordinate for sh in shots]
        if shot_coordinate in list_of_all_shots:
            return True

        return False

    def check_shot_for_hit(self, shot):
        ship = self.check_ship_presence_for_cell(
            shot.coordinate, self.not_active_player.ships
        )

        if ship:
            if self.mark_ship_as_destroyed(ship):
                self.check_for_win_game()

            return True

        return False

    @staticmethod
    def check_correct_cell_index(cell_index):
        if (cell_index[0] < 0) or \
           (cell_index[1] < 0) or \
           (cell_index[0] > 9) or \
           (cell_index[1] > 9):
            return False

        return cell_index

    def add_surround_shots(self, ship):
        for cell in ship.full_coordinates:
            neighbor_cells = [
                [cell[0]-1, cell[1]-1],
                [cell[0]-1, cell[1]],
                [cell[0], cell[1]-1],
                [cell[0]+1, cell[1]],
                [cell[0], cell[1]+1],
                [cell[0]-1, cell[1]+1],
                [cell[0]+1, cell[1]-1],
                [cell[0]+1, cell[1]+1],
            ]

            # make list of correct (in range of field) neighbor cells
            correct_neighbor_cells = []
            for neighbor_cell in neighbor_cells:
                correct_neighbor_cell = self.check_correct_cell_index(
                    neighbor_cell)

                if correct_neighbor_cell:
                    correct_neighbor_cells.append(correct_neighbor_cell)

            for correct_neighbor_cell in correct_neighbor_cells:
                if not self._check_shot_coordinate_presence(
                        correct_neighbor_cell, self.active_player.shots):
                    if not self.check_ship_presence_for_cell(
                            correct_neighbor_cell, self.active_player.ships):
                        new_shot = Shot(correct_neighbor_cell)
                        self.active_player.shots.append(new_shot)

    def check_for_win_game(self):
        for ship in self.not_active_player.ships:
            if not ship.padded:
                return False

        self.stage = "active_player_wins"

    def make_full_ship_coordinates(self, start_ship_coordinate,
                                   end_ship_coordinate):
        # if we got 1 cell ship
        if start_ship_coordinate == end_ship_coordinate:
            return [start_ship_coordinate]

        return self.make_coordinate_interval(
            start_ship_coordinate, end_ship_coordinate
        )

    def place_ships(self):
        # ships_by_rules = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        ships_by_rules = [4]

        for ship in ships_by_rules:
            self.render_field(
                field=self.active_player.field,
                field_type="Opposite",
                ships=self.active_player.ships,
                opposite_ships=None,
                shots=None,
            )

            while True:
                try:
                    print(ship, "deck ship.")
                    start_ship_coordinate = self.input_while_correct(
                        "Enter ship START coordinates (e.g. A4, B9, C5):"
                    )
                    end_ship_coordinate = self.input_while_correct(
                        "Enter ship END coordinates (e.g. A4, B9, C5):"
                    )
                    full_ship_coordinates = self.make_full_ship_coordinates(
                        start_ship_coordinate,
                        end_ship_coordinate
                    )

                    self.check_correct_ship_position(
                        start_ship_coordinate,
                        end_ship_coordinate,
                        full_ship_coordinates,
                        ship
                    )
                    break
                except SyntaxError as msg:
                    print(msg, "\n")

            new_ship = Ship(
                start_ship_coordinate,
                end_ship_coordinate,
                full_ship_coordinates
            )

            # debug
            # new_ship = Ship([0, 0], [0, 3],
            #                 self.make_full_ship_coordinates([0, 0], [0, 3]))
            # self.active_player.ships.append(new_ship)
            # new_ship = Ship([2, 2], [2, 2],
            #                 self.make_full_ship_coordinates([2, 2], [2, 2]))
            # self.active_player.ships.append(new_ship)

            self.active_player.ships.append(new_ship)

            self.render_field(
                field=self.active_player.field,
                field_type="Opposite",
                ships=self.active_player.ships,
                opposite_ships=None,
                shots=None,
            )

    def make_move(self):
        if self.stage == "data_input":
            self.activate_player()

            self.active_player.field = Field()
            self.place_ships()

            if self.not_active_player:
                self.stage = "game"
        elif self.stage == "game":
            self.change_players()
            print(self.active_player, "turn")

            # rendering own filed
            self.render_field(
                field=self.active_player.field,
                field_type="Own",
                ships=self.active_player.ships,
                opposite_ships=None,
                shots=self.not_active_player.shots,
            )

            # rendering opposite field
            self.render_field(
                field=self.not_active_player.field,
                field_type="Opposite",
                ships=None,
                opposite_ships=self.not_active_player.ships,
                shots=self.active_player.shots,
            )

            shot = self.make_shot()
            if self.check_shot_for_hit(shot):
                print("Successful hit.")
                self.change_players()

            if self.stage == "active_player_wins":
                return False

        return True


def main():
    global input_function
    input_function = get_input_function()
    game = Game()

    while True:
        if not game.make_move():
            break

    print("\n\n\nYou win!\n\n\n")

if __name__ == '__main__':
    main()
