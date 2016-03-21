import collections
import string

def_size = 10

# DICT = collections.OrderedDict()
# d = {value: value+1 for value in range(def_size)}

# print(d)


# DICT.update({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10})
# DICT = collections.OrderedDict(sorted(DICT.items(), key=lambda t: t[0]))

# from pprint import pprint
# pprint(DICT)

DICT = {char: string.ascii_uppercase.index(char)+1 for char in string.ascii_uppercase[0:def_size]}
DICT = collections.OrderedDict(sorted(DICT.items(), key=lambda t: t[0]))
print(DICT)