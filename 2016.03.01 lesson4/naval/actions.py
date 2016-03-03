# -*- coding: utf-8 -*-

from __future__ import print_function

from utils import get_input_function
from models import Player

class BaseAction(object):
    input_function = get_input_function()

class MoveAction(BaseAction):
    number = 0
    player = None

    def _add_player(self, storage, current_player_number):
        if storage.current_player is None:
            current_player_number = 1
        elif len(storage.players) is 1:
            current_player_number = 2
        else:
            raise IndexError("В этой игре может быть только 2 игрока!")

        current_player = Player()
        current_player.name = self.input_function('Input name for player', current_player_number, ': ')
        storage.players.append(current_player)


    def _make_ships_for_player(self, storage):
        # 1 ship 4 cells, 2 ships 3 cells, 3 ships 2 cells and 4 ships 1 cell
        # for current player
        pass

    def get_players_by_number(self, storage, current_player_number):
        pass

    def render(self, current_player, opposite_player_field):
        pass

    def perform_move(self, storage):
        if storage.stage is "data_input":
            self._add_player(storage)
            self._make_ships_for_player(storage)

            if len(storage.players) == 2:
                storage.stage = "game"

            return
        elif storage.stage is "game":
            current_player, opposite_player = self.get_players_by_number(storage, current_player_number)
            self.render(current_player, opposite_player.field)