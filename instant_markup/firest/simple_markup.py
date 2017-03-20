#encoding:utf-8
import sys,re
from util  import *

print '<html><head><title>  hello </title></head><body>'
#<em> 标签告诉浏览器把其中的文本表示为强调的内容。对于所有浏览器来说，这意味着要把这段文字用斜体来显示。
title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        print '<h1>'
        print block 
        print '</h1>'
        title = False
    else:
        print '<p>'
        print block 
        print '</p>'
print '</body></html>'


'''

 python simple_markup.py  < test_input.txt > out.html


*World Wide Spam* 把这些变成 强调 ，对于所有浏览器来说，这意味着要把这段文字用斜体来显示

这里我们需要注意一下，re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)，他是re模块的应用，首先增则匹配到内容，然后替换式替换。
其他部分，就是判断title是否为True，若是则给h1标签，否则给p标签。

其中re.sub是正则表达式，将*XXX*替换为：<em>XXX</em>
正则表达式讲解可见：http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

参考 
python基础教程笔记-项目1-即时标记-Day1
http://m.blog.csdn.net/article/details?id=43088495

python基础教程笔记-项目1-即时标记-Day2
http://m.blog.csdn.net/article/details?id=43114555




'''        
