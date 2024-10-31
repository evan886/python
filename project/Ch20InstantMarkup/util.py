def lines(file):
    for line in file: yield line 
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif  block:
            yield ''.join(block).strip()
            block = []



#     lines函数
#         函数定义
#             函数lines接受一个参数file，这里的file通常是一个文件对象（例如通过open函数打开文件得到的对象）。
#         循环和生成器
#             for line in file: yield line：这是一个循环，它遍历文件中的每一行。yield关键字使得这个函数成为一个生成器。每次调用生成器的__next__方法（通常在for循环中隐式调用），它会返回文件中的下一行。
#             yield '\n'：在遍历完文件中的所有行之后，这个函数还会生成一个换行符。这是为了在处理文件结束时，确保有一个类似行结束的标识。
#     blocks函数
#         初始化
#             函数blocks也接受一个文件对象file作为参数。它首先初始化一个空列表block，这个列表用于临时存储从文件中读取的行。
#         循环处理
#             for line in lines(file):：这里调用了lines函数来逐行获取文件内容。
#             条件判断：
#                 if line.strip():：检查当前行去除首尾空白字符（包括空格、制表符、换行符等）后是否为空。如果不为空，说明这一行有实际内容，将其添加到block列表中（block.append(line)）。
#                 elif block:：如果当前行是空行（line.strip()为False），并且block列表不为空，这意味着一个块已经结束。此时，yield ''.join(block).strip()会将block中的所有行连接成一个字符串（''.join(block)），然后去除这个字符串首尾的空白字符，并将其作为一个块返回（通过yield），最后将block重置为空列表（block = []），准备处理下一个块。


# 例如，假设有一个文本文件test.txt内容如下：


# plaintext
# 复制

# This is the first block.
# It has multiple lines.

# This is the second block.


# 使用blocks函数处理这个文件时：

#     首先，读取This is the first block.和It has multiple lines.，因为它们之间没有空行，所以会被累积在block列表中。
#     当遇到空行时，block中的内容会被连接成一个字符串（去除首尾空白字符后）并返回，然后block被清空。
#     接着读取This is the second block.，它会被累积在新的block中，直到下一个空行或者文件结束。

