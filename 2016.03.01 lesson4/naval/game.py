# -*- coding: utf-8 -*-

from __future__ import print_function

from models import Field
from player import Player
from utils import get_input_function
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

    def activate_player(self):
        # name = input_function('Input player ' + str(len(self.players) + 1) + " name: ")
        name = "Alex"
        current_player = Player(name)
        self.players.append(current_player)
        self.active_player = current_player

    @staticmethod
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

    def make_coordinate_interval(self, ship):
        x_interval = self.make_skipped_numbers(ship.start_coordinate[0], ship.end_coordinate[0])
        y_interval = self.make_skipped_numbers(ship.start_coordinate[1], ship.end_coordinate[1])

        if x_interval and y_interval:
            raise SyntaxError("Logic error! You can't have both X and Y coordinates increament!")

        if x_interval:
            return [ [x_coord, ship.start_coordinate[1]] for x_coord in x_interval ]
        elif y_interval:
            return [ [ship.start_coordinate[0], y_coord] for y_coord in y_interval ]
        else: # start_coordinate == end_coordinate
            return ship.start_coordinate

    def render_field(self, field=[], ships=[], shots=[]):
        rendered_field = []

        for x in range(field.size[0]):
            rendered_field.append([])
            for y in range(field.size[1]):
                rendered_field[x].append(".")

        for ship in ships:
            for coordinate in self.make_coordinate_interval(ship):
                rendered_field[coordinate[1]][coordinate[0]] = "O"

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

    # def place_ships_for_active_player(self):
    #     pass

    def make_move(self):
        if self.stage == "data_input":
            self.activate_player()
            self.active_player.field = Field()
            self.active_player.place_ships(self.render_field)

            if len(self.players) == 2:
                self.stage = "game"
        elif self.stage == "game":
            self.active_player.make_shot()

        # self.render_field(
        #     self.active_player.field,
        #     self.active_player.ships,
        #     self.active_player.shots
        # )



def main():
    game = Game()

    while True:
        game.make_move()
        exit()


        # if game.stage == "game":
        #     game.make_move()
        #     break

        # try:
        #     command = parse_user_input()
        #     perform_command(command)
        # except UserExitException:
        #     break
        # except KeyboardInterrupt:
        #     print('Shutting down, bye!')
        #     break

if __name__ == '__main__':
    input_function = get_input_function()

    main()