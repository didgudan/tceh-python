# -*- coding: utf-8 -*-

from __future__ import print_function

from models import Field
from player import Player
from utils import get_input_function, make_skipped_numbers
from consts import DICT


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
        self.players = []
        self.active_player = None
        self.not_active_player = None

    def _check_player_name_identity(self, second_player_name):
        if not self.active_player:
            return

        if self.active_player.name == second_player_name:
            raise SyntaxError("Players name can't be same!")

    def change_players(self):
        self.active_player, self.not_active_player = self.not_active_player, self.active_player
        print("\n", self.active_player, "turn", "\n")

    def activate_player(self):
        # while True:
        #     try:
        #         name = input_function('\nInput player ' + str(len(self.players) + 1) + " name: ")
        #         self._check_player_name_identity(name)
        #         break
        #     except SyntaxError as msg:
        #         print(msg)

        name = "Alex"
        if self.active_player:
            name = "Alex_clone"

        current_player = Player(name)
        self.players.append(current_player)
        self.not_active_player = self.active_player
        self.active_player = current_player
        print("\n", self.active_player, "turn", "\n")

    @staticmethod
    def make_coordinate_interval(ship):
        x_interval = make_skipped_numbers(ship.start_coordinate[0], ship.end_coordinate[0])
        y_interval = make_skipped_numbers(ship.start_coordinate[1], ship.end_coordinate[1])

        if x_interval and y_interval:
            raise SyntaxError("Logic error! You can't have both X and Y coordinates increament!")

        if x_interval:
            return [[x_coord, ship.start_coordinate[1]] for x_coord in x_interval]
        elif y_interval:
            return [[ship.start_coordinate[0], y_coord] for y_coord in y_interval]

    def render_field(self, field=[], ships=[], shots=[], field_name="Own"):
        print(field_name,"field:\n")

        rendered_field = []

        for x in range(field.size[0]):
            rendered_field.append([])
            for y in range(field.size[1]):
                rendered_field[x].append(".")

        for ship in ships:
            # if we got 1 cell ship
            if ship.start_coordinate == ship.end_coordinate:
                rendered_field[ship.start_coordinate[1]][ship.start_coordinate[0]] = "O"
                continue

            for coordinate in self.make_coordinate_interval(ship):
                rendered_field[coordinate[1]][coordinate[0]] = "O"

        for shot in shots:
            rendered_field[shot.coordinate[1]][shot.coordinate[0]] = "x"

        # add all keys in DICT as first list in render_field
        rendered_field.insert(0,
            list(DICT.keys())
        )
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

    def make_move(self):
        if self.stage == "data_input":
            self.activate_player()
            self.active_player.field = Field()
            self.active_player.place_ships(self.render_field)

            if len(self.players) == 2:
                self.stage = "game"
        elif self.stage == "game":
            self.change_players()

            self.render_field(
                self.active_player.field,
                self.active_player.ships,
                self.not_active_player.shots,
                "Own"
            )
            self.render_field(
                self.not_active_player.field,
                [],
                self.active_player.shots,
                "Opposite"
            )

            self.active_player.make_shot()


def main():
    global input_function
    input_function = get_input_function()
    game = Game()

    while True:
        game.make_move()

if __name__ == '__main__':
    main()