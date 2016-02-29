from __future__ import print_function

import pickle
import os.path
import glob


SAVE_PATH = "tasks"

class Test(object):
    a = ""
    b = ""

# t1 = Test()
# t1.a = "value t1.a"
# t1.b = "value t1.b"

# t2 = Test()
# t2.a = "value t2.a"
# t2.b = "value t2.b"

# objects = [t1, t2]

# while True:
#     try:
#         if not os.path.exists(SAVE_PATH):
#             os.makedirs(SAVE_PATH)

#         filename = raw_input('Input filename to save data: ')
#         filename = SAVE_PATH + "/" + filename + ".task"
#         if os.path.isfile(filename): 
#             raise SyntaxError
#         with open(filename, 'w') as outfile:
#             pickle.dump(objects, outfile, pickle.HIGHEST_PROTOCOL)
#         break
#     except IOError:
#         print('Can\'t create such file!')
#     except SyntaxError:
#         print('File ', filename, 'already exist!')


working_directory = os.getcwd()

os.chdir(SAVE_PATH)

files = glob.glob("*.task1")
if len(files) < 1:
    print('There are no saved files!')
    exit()
    
print(files)
exit()

while True:
    try:
        filename = raw_input('Input filename to load data: ')
        if not os.path.isfile(filename): 
            raise SyntaxError
        with open(filename, 'rb') as infile:
            objects = pickle.load(infile)
        break
    except SyntaxError:
        print('There is no such file!')

for obj in objects:
    print(objects)

os.chdir(working_directory)