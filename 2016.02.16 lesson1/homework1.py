# -*- coding: UTF-8 -*-

import sys

questions_and_answers = [
    ['Как сказать питону что это утварждение ложь', 'False', 'str'],
    ['Выберите правильный ответ: конкретинация(1) или конкатенация(2)', '2', 'int'],
    ['Хм, где же я видел эту забавную картину с осьминого-котом', 'github', 'str'],
    ['Ничто в питоне', 'None', 'str'],
    ['Всё в питоне', 'object', 'str'],
    ['Юни..., uni.... что-что, простите', 'unicode', 'str'],
    ['Где плавает точка', 'float', 'str'],
    ['А! Где я', 'tceh', 'str'],
]

if sys.version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input

rus_types = {'int': 'число', 'str': 'строка', 'float': 'число с плавающей точкой'}
tries = 0
current_num = 0

print("\nИмейте в виду, что вы находитесь на занятии, ответы это всегда ОДНО английское слово по существу или число и здесь как питон -- регистр имеет значение!\n")

while current_num < len(questions_and_answers):
    current_elem = questions_and_answers[current_num]
    user_answer = input_function(str(current_elem[0]) + " (" + rus_types[current_elem[2]] + ")? ")

    try:
       eval(current_elem[2] +  "('" + user_answer + "')") ## ugly hack, но как по-другому здесь использовать именно try/except я не придумал, проще было бы это сделать с помощью if/else :(
    except ValueError:
        tries += 1
        print("Некорректный тип ответа! Вам же русским языком напечатано (в скобках) какой тип ответа должен быть!")
        continue

    if user_answer == current_elem[1]: 
        current_num += 1
        print("Верно! Продолжаем.\n") 
    else: 
        tries += 1
        print("Ответ неверный, попробуйте ещё раз.") 

print("")
if tries is 0: print("Поздравляю, вы ответили на все загадки в этот раз с первой попытки! Наверное видели код или вы это я? :)")
else: print("Всего вы не угадали: " + str(tries) + " раз(а).")