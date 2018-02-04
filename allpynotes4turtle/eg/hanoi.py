#-*-coding:utf-8-*-
def hanoi(n,x,y,z):
    if n ==1:
        print(x,'-->',z)
    else:
        #思路明白了 但是只是是不明白这个z 在这里干啥 
        hanoi(n-1,x,z,y)# 将前n-1 个盘子从x 移动到y 上
        print(x,'-->',z) #将最底下的最后一个身子从x 移动到z上 
        hanoi(n-1,y,x,z)#将y上的n-1 个盘子移动到z上
n = input('pleas ')
hanoi(n,'x','y','z')
"""
pleas 3
('x', '-->', 'z')
('x', '-->', 'y')
('z', '-->', 'y')
('x', '-->', 'z')
('y', '-->', 'x')
('y', '-->', 'z')
('x', '-->', 'z')
"""