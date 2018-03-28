Python字符与数字的相互转换

[ chr(x) for x  in range(97,123)] 


 chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
 返回值
返回值是当前整数对应的ascii字符

对于ASCII字符,可以使用内建的ord和chr方法实现需求:

>>> chr(97)
'a'
>>> ord('a') 
97

对于Unicode字符,需要使用ord和repr,获得unicode字符的方法,使用unichr:

>>> print ord(u'\u2020') 
8224 
>>> print repr(unichr(8224)) 
u'\u2020'




[https://blog.csdn.net/oatnehc/article/details/6690553 PYTHON字符与数字的相互转换 ]

 [http://www.runoob.com/python/python-func-chr.html Python chr() 函数  ]

 [https://blog.csdn.net/youfuchen/article/details/21107099  python chr()和ord()]

 [https://blog.csdn.net/littlebo01/article/details/23283997 用python把数字转换成字母]
