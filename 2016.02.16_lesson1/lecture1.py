# -*- coding: utf-8 -*-	

import sys

print(sys.version_info)
print("int is object:", isinstance(3, object))
print("True is object:", isinstance(True, object))
print("None is object:", isinstance(None, object))
print("isinstance is object:", isinstance(isinstance, object))