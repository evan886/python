def Fun1():
    x = 5
    def Fun2():
        x *= x
        return x
    return Fun2()
print Fun1()
