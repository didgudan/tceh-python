import sys

print(sys.version_info)

if sys.version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input

while True:
    user_input = input_function("Please, input positive numbers: ")
    user_input = float(user_input)
    if user_input > 0:
        print("Your number is: %d" % user_input)
    else:
        print("%d is a wrong number." % user_input)