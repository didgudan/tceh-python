# -*- coding: UTF-8 -*-

# String types:
print("This is a string.")
print("This is also a string.")

print("We are queal" == 'We are equal')

print(r"This is raw string.")
# print(u'Я -- русская строка!')
print(b"I am a byte array")

print("""
This string contains multiline
	text. And extra spaces. And a \t tab;
""")

# Escape chars:
print('I\'m multiplie string \n too. With extra \t tab.')
print("I'm multiplie string witj escaped \".")
print('I am noisy! \a')

# Casting to string:
print(str(4))
print(str(4 + 1))
print(str(4) + '1')
print(str(None), str(True), str(False), str(object))

# String operations:
print('123' + "456")
print("4" * 4)

print('Chars'[0], "123"[1], 'abc'[-1])
print("Cut me"[0:3])
print("Cut last two chars"[:-2])

print('My name is %s.' % 'Monty')
print("I'm %d years old and %10.3f meters tall." % (49, 1.93))
print('It is also possible to use {2} funcion, with {1} or more args {0}.'.format('format()', 1, 2))

print(len('7 chars'))