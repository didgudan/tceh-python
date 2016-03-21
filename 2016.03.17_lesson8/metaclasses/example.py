import six

class AutonamingType(type):
    def __init__(cls, name, bases, attrs):
        # print(cls, name, bases, attrs)
        for k, v in six.iteritems(attrs):
            if getattr(v, '__autoname__', False) and not v.name:
                v.name = k


class Autonamer(six.with_metaclass(AutonamingType)):
    pass


class Field(object):
    __autoname__ = True

    def __init__(self, name=None):
        self.name = name

    def do_something(self):
        if self.name is None:
            raise ValueError('name is None')
        print(self.name)


class UglyForm(object):
    my_field1 = Field('my_field1')
    my_field2 = Field()


class PrettyForm(Autonamer):
    my_field1 = Field()
    my_field2 = Field('custom_name')


if __name__ == '__main__':
    ugly = UglyForm()
    pretty = PrettyForm()

    ugly.my_field1.do_something()
    try:
        ugly.my_field2.do_something()
    except ValueError as e:
        print(e)

    pretty.my_field1.do_something()
    pretty.my_field2.do_something()
