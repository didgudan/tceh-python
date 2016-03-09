import collections
DICT = collections.OrderedDict()

DICT.update({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10})
DICT = collections.OrderedDict(sorted(DICT.items(), key=lambda t: t[0]))