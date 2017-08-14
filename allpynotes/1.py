class Base1:
    def foo1(self):
        print("I am  foo1, I wei Base1 daiyan")

class Base2:
    def foo2(self):
        print("I am foo2, I wei  Base2 daiyan")
class C(Base1,Base2):
    pass

c = C()
c.foo1()
c.foo2()
