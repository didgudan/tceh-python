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
        # check all storage players for numbers

        storage.player.name = self.input_function('Input name for player', current_player_number, ': ')


    def _make_ships_for_player(self, storage, current_player_number):
        # 1 ship 4 cells, 2 ships 3 cells, 3 ships 2 cells and 4 ships 1 cell
        # for current player
        pass

    def get_players_by_number(self, storage, current_player_number):
        pass

    def render(self, current_player, opposite_player_field):
        pass

    def perform_move(self, storage, current_player_number):
        if storage.stage is "data_input":
            self._add_player(storage, current_player_number)
            self._make_ships_for_player(storage, current_player_number)
            storage.stage = "game"
            return
        elif storage.stage is "game":
            current_player, opposite_player = self.get_players_by_number(storage, current_player_number)
            self.render(current_player, opposite_player.field)