#!/usr/bin/python
class myclass():
    first = 123
    second = 456
    def fu(self):
        return 'test'
        #print "i am function"

if __name__ == "__main__":
    myclass1 = myclass()
    print myclass1.fu()
    print myclass1.first
