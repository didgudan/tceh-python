# -*- coding: utf-8 -*-

from __future__ import print_function
import random  # see https://docs.python.org/2/library/random.html
import sys

EMPTY_MARK = ' '


def shuffle_field():
    # """
    # This method is used to create a field at the very start of the game.
    # :return: list with 16 randomly shuffled tiles,
    # one of which is a empty space.
    # """
    # ...
    tag_list = list(range(0, 15))
    tag_list.append(EMPTY_MARK)
    random.shuffle(tag_list)
    
    # tag_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, EMPTY_MARK, 12, 13, 14, 11]
    
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
        if not field.index(elem) == elem: return False

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
    ## current_position[0] - horizontal index, current_position[1] - vertical index
    current_position = [ int(float(current_index) / 4) + 1, current_index%4 + 1 ]

    if (key is "w"): new_position = [ current_position[0] - 1, current_position[1] ]
    elif (key is "s"): new_position = [ current_position[0] + 1, current_position[1] ]
    elif (key is "a"): new_position = [ current_position[0], current_position[1] - 1 ]
    elif (key is "d"): new_position = [ current_position[0], current_position[1] + 1 ]
    elif (key == "exit"): raise SystemExit
    else:
        raise IndexError("Неизвестный ход!")

    if can_i_move(new_position):
        current_key, new_key = get_key_by_position(current_position), get_key_by_position(new_position)
        field[current_key], field[new_key] = field[new_key], field[current_key]
    else:
        raise IndexError("Туда нельзя!")

    return field


def handle_user_input():
    # """
    # Handles user input. List of accepted moves:
    # 'w' - up, 's' - down,
    # 'a' - left, 'd' - right
    # :return: <str> current move.
    # """
    # ...
    if sys.version_info[0] == 2:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function("\nВаш ход (wsad): ")

    return user_input


def main():
    # """
    # The main method.
    # :return: None
    # """current_string = 
    tag_list = shuffle_field()
    
    print("Для выхода наберите exit.\n")
    
    while not is_game_finished(tag_list):
        try:    
            print_field(tag_list)    
            move = handle_user_input()
            tag_list = perform_move(tag_list, move)
        except Exception as ex:
            print(ex, "\n")
        except SystemExit as ex:
            print("\nДо свиданья!\n")
            exit()
        
    print_field(tag_list)
    print("\nТадам! Вы победили!\n")

# see http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__': 
    main()