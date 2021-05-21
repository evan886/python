#!/usr/bin/python3
class Person:
    def __init__(self, name):
        self.name = name

    def height(self, m):
        h = dict((["height", m],))
        return h

    def breast(self, n):
        b = dict((["breast", n],))
        return b


class Girl(Person):
    def get_name(self):
        return self.name


if __name__ == "__main__":
    xi = Girl("xime")
    print(xi.get_name)
    print(xi.get_name())
    print(xi.height(163))
    print(xi.breast(90))

"""
<bound method Girl.get_name of <__main__.Girl object at 0x7f77eedbe100>>
xime
{'height': 163}
{'breast': 90}


"""
