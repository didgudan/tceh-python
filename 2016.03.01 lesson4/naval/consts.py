import collections
import string

EMPTY_MARK = "."
SHIP_MARK = "o"
MISS_SHOT = "x"
HIT_SHOT = "v"

DEFAULT_FIELD_SIZE = 10

DICT = collections.OrderedDict()
num = 0
for char in string.ascii_uppercase[0:DEFAULT_FIELD_SIZE]:
    DICT[char] = num + 1
    num += 1
