import sys

## зачем нужен размер 24 бита для 1?

print("size of 0 = ", sys.getsizeof(0))
print("size of 1 = ", sys.getsizeof(1))
print("size of 1000000 = ", sys.getsizeof(1000000))

print('size of max_int - 1 = ', sys.getsizeof(sys.maxsize - 1))
print('size of max_int = ', sys.getsizeof(sys.maxsize))