#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect
import sys

from my_module import my_function


def test_for_small_numbers():
    result = my_function(1)
    assert result == False

def test_for_big_numbers():
    result = my_function(3)
    assert result == True

def test_for_equivalence():
    result = my_function(2)
    assert result == True

def test_for_type():
    try:
        result = my_function("abc")
        assert False
    except TypeError:
        assert True

def wrap(func):
    try:
        func()
    except AssertionError:
        return False
    else:
        return True


def run():
    members = inspect.getmembers(sys.modules[__name__])
    test_functions = [obj for name, obj in members
                     if (inspect.isfunction(obj) and name.startswith('test'))]
    return all(wrap(f) for f in test_functions)


if __name__ == '__main__':
    result = run()
    if result:
        print('Passed')
    else:
        print('Failed')
