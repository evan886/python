class CalTest:
    def callback(self,prefix,name,*args):
        method = getattr(self,prefix+name,None)
        if callable(method):return method(*args)
    def printSum(self,*arg):
        sum = 0
        for i in arg:
            sum = sum + i
        return sum