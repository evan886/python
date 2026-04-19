from util import blocks

with open('1.txt','r',encoding='utf-8') as f:
    for block in blocks(f):

        print("--- 一个块---")
        print(block)
        print()



        '''
        blocks() 和 lines() 写在同一个文件里，所以 blocks() 内部可以直接使用 lines()
        '''