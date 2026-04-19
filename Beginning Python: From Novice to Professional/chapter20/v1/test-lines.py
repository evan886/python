# from util import lines
# or add fun below   not  blow

def lines(file):
    """
    生成器：逐行读取文件，最后多输出一个空行
    :param file:
    :return:
    """
    for line  in file:
        yield line
    yield '\n'  #  只有当上面 的 文件读完了，没有下一行了！循环结束。 才执行这一行


with open('1.txt','r',encoding='utf-8') as f:
    for line  in lines(f):
        print(line,end='')



"""
 python test-lines.py >1
➜  v1 git:(master) ✗ cat -A 1
Line 1$
Line 2$
$
Line 3$

"""