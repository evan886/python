#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Foo:
    lang = "java"

    def __init__(self):
        self.lang = "python"

    def getc(cls):
    #def get_class_attr(cls):
        
        return cls.lang


if __name__ == "__main__":
    print("Foo.lang:", Foo.lang)
    r = getc(Foo)
    r = get_class_attr(Foo)
    print("get class attribute:", r)
    f = Foo()
    print("instance attribute:", f.lang)
