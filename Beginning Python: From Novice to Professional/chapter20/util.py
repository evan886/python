def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if  line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block=[]

'''

def lines(file):
    for line in file:        # 1. 循环读取文件里**每一行**
        yield line           # 2. 每次返回一行
                             # 3. 文件读完了 → 循环自动结束
    yield '\n'               # 4. 循环结束后，**最后再额外返回一个空行**

'''
