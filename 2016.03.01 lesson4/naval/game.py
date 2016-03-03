# -*- coding: utf-8 -*-

from __future__ import print_function

from models import Storage, Player
from actions import MoveAction

def main():
    storage = Storage()
    move = MoveAction()

    # player1 = Player()
    # player2 = Player()

    while True:

        move.perform_move(storage)


        # try:
        #     command = parse_user_input()
        #     perform_command(command)
        # except UserExitException:
        #     break
        # except KeyboardInterrupt:
        #     print('Shutting down, bye!')
        #     break

if __name__ == '__main__':
    main()