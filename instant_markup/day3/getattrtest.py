#encoding: utf-8
class Test:
    def print_hello(self):
        print 'func print_hello work'
        
a = Test()
b = getattr(a,'print_hello',None)

print b  # 打印func出属性
b()  # func print_hello work
#前两行的输出是这个决定的 

b = getattr(a,'NoFunc',None)
#print b
'''
<bound method Test.print_hello of <__main__.Test instance at 0x7f7ac1921bd8>>
func print_hello work
None

第一次使用getattr函数时，b尝试获取a中的print_hello函数，从打印结果可看出获取成功之后我们调用了b。

第二次使用getattr函数时，b尝试获取a中的NoFunc函数，从打印结果可看出a中并没有名为NoneFunc的函数，因此b的值为None 

'''        