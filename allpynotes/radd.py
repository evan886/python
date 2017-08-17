class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self,other)

a = Nint(5)
b = Nint(3)
print a + b
# 8
print 1 + b
#2
