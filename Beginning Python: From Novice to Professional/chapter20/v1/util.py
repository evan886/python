def lines(file):
    """
    生成器：逐行读取文件，最后多输出一个空行
    :param file:
    :return:
    """
    for line  in file:
        yield line
    yield '\n'  #  只有当上面 的 文件读完了，没有下一行了！循环结束。 才执行这一行

def blocks(file):
    """"
    生成器：将文本分割成"块"（段落）
    空行分隔不同的块
    """
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []