# -*- coding: utf-8 -*-

from __future__ import print_function

from models import Field, Shot
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
        self.active_player = None
        self.not_active_player = None

    def _check_player_name_identity(self, second_player_name):
        if not self.active_player:
            return

        if self.active_player.name == second_player_name:
            raise SyntaxError("Players name can't be same!")

    def change_players(self):
        self.active_player, self.not_active_player = self.not_active_player, self.active_player
        if self.not_active_player:
            print(self.active_player, "turn")

    def activate_player(self):
        # while True:
        #     try:
        #         name = input_function('\nInput player name: ')
        #         self._check_player_name_identity(name)
        #         break
        #     except SyntaxError as msg:
        #         print(msg)

        name = "Alex"
        if self.active_player:
            name = "Alex_clone"

        if self.active_player:
            self.change_players()

        self.active_player = Player(name)
        print(self.active_player, "turn")

    @staticmethod
    def render_field(field=[], ships=[], shots=[], field_name="Own"):
        print(field_name,"field:\n")

        rendered_field = []

        for x in range(field.size[0]):
            rendered_field.append([])
            for y in range(field.size[1]):
                rendered_field[x].append(".")

        for ship in ships:
            for coordinate in ship.full_coordinates:
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

    def check_ship_presence_for_cell(self, cell):
        for ship in self.not_active_player.ships:
            if cell in ship.full_coordinates:
                return True

        return False

    def check_shot_for_hit(self, shot):
        if self.check_ship_presence_for_cell(shot.coordinate):
            # self.fill_neighbor_free_cells(shot.coordinate)
            return True

        return False

    @staticmethod
    def check_correct_cell_index(cell_index):
        if (cell_index[0]-1 < 0) or \
           (cell_index[1]-1 < 0) or \
           (cell_index[0]+1 > 9) or \
           (cell_index[1]+1 > 9):
            return False

        return cell_index

    def fill_neighbor_free_cells(self, cell):
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
            correct_neighbor_cell = self.check_correct_cell_index(neighbor_cell)
            if correct_neighbor_cell:
                correct_neighbor_cells.append(correct_neighbor_cell)

        for neighbor_cell in correct_neighbor_cells:
            if neighbor_cell not in self.active_player.shots:
                if not self.check_ship_presence_for_cell(neighbor_cell):
                    new_shot = Shot(neighbor_cell)
                    self.active_player.shots.append(new_shot)

    def check_for_win_game(self):
        pass

    def make_move(self):
        if self.stage == "data_input":
            self.activate_player()

            self.active_player.field = Field()
            self.active_player.place_ships(self.render_field)

            if self.not_active_player:
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

            shot = self.active_player.make_shot()
            if self.check_shot_for_hit(shot):
                self.change_players()

            if self.check_for_win_game():
                return True


def main():
    global input_function
    input_function = get_input_function()
    game = Game()

    while True:
        game.make_move()

    print("\n\n\nYou win!\n\n\n")

if __name__ == '__main__':
    main()