# -*- coding: UTF-8 -*-

import pdb

list1 = [1, 2, 3]
list2 = list1[:]

pdb.set_trace()

list1.append(2)
print('list1 is: ' + str(list1) + " and list2 is: " +  str(list2))
