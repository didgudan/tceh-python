import collections
import string

DEFAULT_FIELD_SIZE = 10

DICT = collections.OrderedDict()
num = 0
for char in string.ascii_uppercase[0:DEFAULT_FIELD_SIZE]:
    DICT[char] = num + 1
    num += 1

