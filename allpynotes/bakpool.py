class Turtle:
    def __init__(self,x):
        self.num = x

class  Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self, x , y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

#    def print_num(self):
#        print("the pool have turtle  %d , filsh %d "  % (self.turtle.num, self.fish.num)
        #print  %(self.turtle.num)

#pool = Pool(1,10)
#pool.print_num()
 
