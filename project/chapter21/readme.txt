pip install reportlab
全改成py3 代码了  要先启动apache2  txt文件我改了一下  哈哈 这样就行了  

https://spawx.nwra.com/spawx/listpredict.html

这里另存为并改的txt文件

https://blog.csdn.net/tommyjsj/article/details/16327143
可能要改一下写法了  

 python3 listing21-2.py 
Traceback (most recent call last):
  File "/home/evan/github/python/project/chapter21/listing21-2.py", line 26, in <module>
    drawing.add(PolyLine(zip(times, pred), strokeColor=colors.blue))
  File "/home/evan/.local/lib/python3.9/site-packages/reportlab/graphics/shapes.py", line 1389, in __init__
    lenPoints = len(points)
TypeError: object of type 'zip' has no len()
evan@myxps:~/github/python/project/chapter21$ python3 listing21-3.py 
Traceback (most recent call last):
  File "/home/evan/github/python/project/chapter21/listing21-3.py", line 1, in <module>
    from urllib import urlopen
ImportError: cannot import name 'urlopen' from 'urllib' (/usr/lib/python3.9/urllib/__init__.py)
:
