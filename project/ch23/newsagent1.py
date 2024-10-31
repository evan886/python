#!/usr/bin/python3.9
from nntplib import NNTP

#servername = 'news.foo.bar'

servername = 'freenews.netfront.net'
group = 'comp.lang.python.announce'
server = NNTP(servername)
howmany = 10

resp, count, first, last, name = server.group(group)

start = last - howmany + 1

resp, overviews = server.over((start, last))
for id ,over in overviews:
    suject = over['subject']
    resp,info = server.body(id)
    print(suject)
    print(''- * len(subject))
    for line in info.lines:
        print(line.decode('utf-8'))
    print()

server.quit()


# server.body 长什么样子
# 如果使用nntplib模块中的server.body(id)方法，它通常返回一个包含文章内容的对象。

# 具体来说，它返回一个包含两个元素的元组，第一个元素通常是服务器的响应状态，第二个元素是一个包含文章具体内容的对象。

# 这个对象通常有一个lines属性，它是一个可迭代对象，包含文章的每一行内容，以字节形式表示。

# 例如，假设我们有一篇文章内容如下：


# plaintext
# 复制

# This is a sample article.
# It has multiple lines.


# 当调用server.body(id)获取这篇文章时，返回的内容可能类似这样：

# (response_status, <object with lines attribute>)，其中lines属性可能是类似这样的可迭代对象：[b'This is a sample article.', b'It has multiple lines.']。

# 实际的返回结果会根据服务器的具体实现和文章的实际内容而有所不同。

