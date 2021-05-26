In [1]: from urllib.request import urlopen
In [2]: webpage= urlopen("http://www.python.org")

In [5]: print(webpage)

#太多 最好不要打印
print(webpage.read())


n [7]: text=webpage.read()

In [8]: import re


https://www.runoob.com/python3/python-urllib.html
