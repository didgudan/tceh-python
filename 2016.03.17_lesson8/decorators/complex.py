from __future__ import print_function

import types

from methods import print_execution_time


class TimingMetaClass(type):
    def __init__(cls, name, bases, attrs):
        for k, v in attrs.items():
            if isinstance(v, types.FunctionType):
                v = print_execution_time(v)
                setattr(cls, k, v)


def class_decorator(verbose=False):
    def wrapper(cls):
        return TimingMetaClass(
            cls.__name__,
            cls.__bases__,
            dict(cls.__dict__),
        )

    return wrapper


@class_decorator(verbose=True)
class Printer(object):
    def print_line(self, value):
        print()
        print(value)

    def print_same(self, value):
        print(value, end=' ')


if __name__ == '__main__':
    p = Printer()
    p.print_same('same;')
    p.print_same('same;')
    p.print_line('new line')
