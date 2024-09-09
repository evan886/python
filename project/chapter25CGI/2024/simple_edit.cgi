#!/usr/bin/env python3

#  chapter 25  项目6：使用CGI进行远程 编辑
# cat /usr/lib/cgi-bin/simple_edit.cgi
# cat /usr/lib/cgi-bin/data/foofile.txt
# dadfa  pass  last


import cgi
form = cgi.FieldStorage()

text = form.getvalue('text',open('simple_edit.dat').read())
f = open('simple_edit.dat','w')
f.write(text)
f.close()


# print("""Content-type: text/html # 手工这个页面有问题 应该是这行吧   500 
print("""Content-type: text/html   

<html>
<head>
   <title>Simple Edit</title>
</head>
<body>
   <form method="post" action="simple_edit.cgi" method="POST">
      <textarea name="text" rows="20" cols="20">{}</textarea> <br />
      <input type="submit" >
   </form>
    </body>
</html>
""".format(text))
