# -*- coding: utf-8 -*-

from __future__ import print_function

from models import Storage, Player
from actions import MoveAction

def main():
    storage = Storage()
    move = MoveAction()

    # player1 = Player()
    # player2 = Player()
    current_player_number = 1

    while True:

        move.perform_move(storage, current_player_number)


        # try:
        #     command = parse_user_input()
        #     perform_command(command)
        # except UserExitException:
        #     break
        # except KeyboardInterrupt:
        #     print('Shutting down, bye!')
        #     break
        if current_player_number is 1: current_player_number = 2
        elif current_player_number is 2: current_player_number = 1


if __name__ == '__main__':
    main()