# -*- coding: utf-8 -*-

from __future__ import print_function
import random  # see https://docs.python.org/2/library/random.html
import sys

EMPTY_MARK = ' '


if sys.version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input


def shuffle_field():
    # """
    # This method is used to create a field at the very start of the game.
    # :return: list with 16 randomly shuffled tiles,
    # one of which is a empty space.
    # """
    # ...
    tag_list = list(range(1, 16))
    tag_list.append(EMPTY_MARK)
    random.shuffle(tag_list)
    
    # tag_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, EMPTY_MARK, 13, 14, 15, 12]
    
    return tag_list


def print_field(field):
    # """
    # This method prints field to user.
    # :param field: current field state to be printed.
    # :return: None
    # """
    # ...

    cur_pos = 1
    while cur_pos <= len(field):
        if cur_pos % 4 == 1: print("[", end="")
        print( 
            "{:>{width}}".format(
                field[cur_pos-1], 
                width=max(2, len(EMPTY_MARK)) ## select max from length of EMPTY_MARK and 2 wich is maximum lenght of digit in tag_list
            ), 
            end=""
        )
        if cur_pos % 4 > 0: print(", ", end="")
        if cur_pos % 4 == 0: print("]")
        cur_pos += 1


def is_game_finished(field):
    # """
    # This method checks if the game is finished.
    # :param field: current field state.
    # :return: True if the game is finished, False otherwise.
    # """
    # ...
    if field[len(field)-1] != EMPTY_MARK: return False

    for elem in field[0:-1]:
        if not field.index(elem) + 1 == elem: return False

    return True    


def get_key_by_position(position):
    return (position[0]-1)*4 + position[1] - 1


def can_i_move(new_position):
    for pos in new_position:
        if not 1 <= pos <= 4: return False
    return True


def perform_move(field, key):
    # """
    # Moves empty-tile inside the field.
    # :param field: current field state.
    # :param key: move direction.
    # :return: new field state (after the move).
    # :raises: IndexError if the move can't me done.
    # """
    # ...
    current_index = field.index(EMPTY_MARK)
    current_position = [ int(float(current_index) / 4) + 1, current_index%4 + 1 ]

    if (key == "w"): new_position = [ current_position[0] - 1, current_position[1] ]
    elif (key == "s"): new_position = [ current_position[0] + 1, current_position[1] ]
    elif (key == "a"): new_position = [ current_position[0], current_position[1] - 1 ]
    elif (key == "d"): new_position = [ current_position[0], current_position[1] + 1 ]
    else:
        pass

    # print(new_position)
    # print(get_key_by_position(new_position))

    if can_i_move(new_position):
        current_key, new_key = get_key_by_position(current_position), get_key_by_position(new_position)
        # print(current_key, new_key)
        field[current_key], field[new_key] = field[new_key], field[current_key]
    else:
        print("Can't do such move!\n")

    return field


def handle_user_input():
    # """
    # Handles user input. List of accepted moves:
    # 'w' - up, 's' - down,
    # 'a' - left, 'd' - right
    # :return: <str> current move.
    # """
    # ...
    pass


def main():
    # """
    # The main method.
    # :return: None
    # """current_string = 
    tag_list = shuffle_field()
    
    while not is_game_finished(tag_list):
        print_field(tag_list)    
        move = input_function("\nВаш ход (wsad): ")
        tag_list = perform_move(tag_list, move)
    
    print("\n\n\nТадам! Вы победили!\n\n\n")

# see http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__': 
    main()