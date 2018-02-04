class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent. '
        print 'Parent'

    def bar(self,message):
        print message, 'from Parent'

class FooChild(FooParent):
    def __init__(self):
        FooParent.__init__(self)
        print 'Child'

    def bar(self,message):
        #FooParent.bar(self,message)
        super(FooChild, self).bar(message)
        print 'Child bar function.'
        print self.parent

if __name__ =='__main__':
    foochild = FooChild()
    foochild.bar('HelloWorld')
        

'''
Parent
Child
HelloWorld from Parent
Child bar function.
I'm the parent. 
'''    
