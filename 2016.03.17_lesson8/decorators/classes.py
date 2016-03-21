
def class_decorator(cls):
    def _inner():
        print(cls)
        cls.modification = 'Modified by a decorator'
        return cls

    return _inner()


@class_decorator
class Decorated(object):

    @classmethod
    def print_class_name(cls):
        print(cls.__name__)

    @staticmethod
    def print_meta():
        print(':: Meta information ::')

    def print_obj(self):
        print(self.modification)


if __name__ == '__main__':
    Decorated.print_meta()
    Decorated.print_class_name()

    d = Decorated()
    d.print_obj()
