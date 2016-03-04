# -*- coding: utf-8 -*-

from __future__ import print_function

from utils import get_input_function
from models import Player, Field

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
        current_player.field = Field()
        storage.players.append(current_player)


    def _make_ships_for_player(self, storage):
        dimensions = [4,3,3,2,2,2,1,1,1,1]
        ships = []
        ship_number = 1
        print('Enter ships coordinates, use space to sepaprate cells')
        while ship_number <= 10:
           print('Ship # ',ship_number)
           print('It has ',dimensions[ship_number-1],'cells')
           coordinates = raw_input().split()
           if len(coordinates)==dimensions[ship_number-1]:
               ships.append(coordinates)
               print('Ship #',ship_number,'of',dimensions[ship_number-1],'created')
               print''
               ship_number+=1
           else:
               print("Coordinates don't fit the ship, try again")
               pass
        print(ships)

    def render(self, storage):
        current_field = []

        full_size = storage.current_player.field.size[0] * storage.current_player.field.size[1]
        for point in full_size:
            current_field.append(".")

        for ship in storage.current_player.ships:
            pass

    def perform_move(self, storage):
        if storage.stage is "data_input":
            self._add_player(storage)
            self._make_ships_for_player(storage)

            if len(storage.players) == 2:
                storage.stage = "game"

            return
        elif storage.stage is "game":
            self.render(storage)