#!/usr/bin/python
# -*- coding: utf-8 -*-  
import sys, re
from util import *

print '<html><head> <title>...</title><body>'

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

# ln 10 r 是原字符串的意思  不全明白   ?  1 why
# 这个不是在py cli 执行的 笨死了    python simple_markup.py < test_input.txt > test_output.html