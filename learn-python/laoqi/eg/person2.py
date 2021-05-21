#!/usr/bin/python3
class Person:
    """
    This is a sample of class.
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def breast(self, n):
        self.breast = n

    def color(self, color):
        print("{0} is {1}".format(self.name, color))

    def how(self):
        print("{0} is {1}".format(self.name, self.breast))


if __name__ == "__main__":
    girl = Person("canglaoshi")
    girl.breast(90)

    girl.color("white")
    girl.how()
"""
python3  eg/person2.py
canglaoshi is white
canglaoshi is 90

"""
