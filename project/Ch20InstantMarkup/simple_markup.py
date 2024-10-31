import sys,re
from util import *

print('<html><head><title>...</title><body>')

title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')

print('</body></html>')


#         from util import *：从util模块中导入所有内容。这里的util模块应该包含了之前定义的blocks函数。
#     HTML 输出开始
#         print('<html><head><title>...</title><body>')：开始输出 HTML 内容，创建了一个基本的 HTML 结构，包括<html>、<head>、<title>（这里标题内容是...，可能需要进一步修改）和<body>标签。
#     处理输入块
#         for block in blocks(sys.stdin):：从标准输入（sys.stdin）读取数据，使用blocks函数将输入数据按块划分。blocks函数可能会根据空行等条件来划分块。
#         对每个块进行处理：
#             block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)：使用正则表达式替换。这个正则表达式r'\*(.+?)\*'的作用是找到块中被*包围的内容。(.+?)是一个非贪婪匹配的组，它会匹配*之间的任意字符。然后将匹配到的内容用<em>和</em>标签替换，<em>标签通常用于表示强调的文本。
#     根据条件输出 HTML 块
#         有一个布尔变量title，初始值为True。
#             如果title为True：
#                 print('<h1>')：输出<h1>标签，用于一级标题。
#                 print(block)：输出处理后的块内容。
#                 print('</h1>')：输出</h1>标签，结束一级标题。
#                 title = False：将title设置为False，这样下一个块就不会被当作标题处理了。
#             否则（即title为False）：
#                 print('<p>')：输出<p>标签，用于段落。
#                 print(block)：输出处理后的块内容。
#                 print('</p>')：输出</p>标签，结束段落。
#     HTML 输出结束
#         print('</body></html>')：结束 HTML 结构，输出</body>和</html>标签。


# 总体来说，这段代码的功能是从标准输入读取文本数据，将文本中的某些格式（这里是*包围的内容）转换为 HTML 格式（<em>标签），并将输入的文本块分别作为 HTML 中的标题（第一个块）和段落（后续块）进行包装，最后输出完整的 HTML 文档。



# re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)

#     函数作用
#         re.sub()是 Python 中re（正则表达式）模块的一个函数，用于在字符串中进行正则表达式的替换操作。
#         在这个例子中，re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)的作用是在block这个字符串中查找所有被*包围的子字符串，并将其替换为用<em>和</em>标签包围的相同内容。
#     正则表达式分析
#         r'\*(.+?)\*'
#             \*：在正则表达式中，\是转义字符，这里\*表示匹配字符*本身。因为*在正则表达式中有特殊含义（表示前面字符的零个或多个重复），所以需要转义。
#             (.+?)：
#                 ()：这是一个分组操作，用于捕获括号内匹配的内容。
#                 .：在正则表达式中，.匹配除换行符\n外的任意字符。
#                 +：表示前面的字符（这里是.）出现一次或多次。
#                 ?：在+后面，表示非贪婪匹配。也就是说，它会尽可能少地匹配字符。例如，对于字符串*abc*def*，贪婪匹配可能会把abc*def都匹配到一个组里，而非贪婪匹配会只匹配abc到一个组里。
#         r'<em>\1</em>'
#             <em>和</em>：这是 HTML 中的强调标签，用于包围需要强调的文本。
#             \1：这是对前面正则表达式中第一个分组（即(.+?)）所匹配内容的引用。在替换时，会将分组所匹配的内容放在\1的位置。


# 例如，如果block字符串是This is *a test* string.，那么经过re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)操作后，会得到This is <em>a test</em> string.。

# 为什么 title = True

#     初始化判断条件
#         在这段代码中，title = True的作用是为了初始化一个用于判断的标志。
#         代码的主要目的是将输入的文本块转换为 HTML 格式。它希望将第一个文本块作为 HTML 中的<h1>标题来处理，而后续的文本块作为<p>段落来处理。
#         通过将title初始化为True，在进入for循环处理第一个文本块时，条件if title:会成立，从而使得第一个文本块被正确地格式化为<h1>标题。
#         然后，在处理完第一个文本块后，代码立即将title设置为False（title = False），这样在后续的循环中，对于其他文本块，if title:条件不成立，就会进入else分支，将它们格式化为<p>段落。


# 总之，title = True是为了设定初始状态，以便正确区分和处理第一个文本块与后续文本块的 HTML 格式化。