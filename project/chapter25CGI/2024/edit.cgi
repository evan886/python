#!/usr/bin/env python3

#  chapter 25  项目6：使用CGI进行远程 编辑
# cat /usr/lib/cgi-bin/dit.cgi
# cat /usr/lib/cgi-bin/data/foofile.txt
# dadfa  pass  last
# chmod  777 edit.cgi  不行 500 
print('Content-type: text/html\n')

from os.path import join,abspath 
import cgi,sys

BASE_DIR = abspath('data')

form = cgi.FieldStorage()
filename = form.getvalue('filename')
if  not filename:
    print('Please enter a  filename ')
    sys.exit()

text = open(join(BASE_DIR,filename)).read()

# print("""Content-type: text/html # 手工这个页面有问题 应该是这行吧   500 
print("""
<html>
<head>
   <title> Editing </title>
</head>
<body>
   <form action="save.cgi" method="POST">
      <b>File </b> {} <br />
      <input type="hidden" name="filename" value="{}" />
      <b> Password</b> <br />
      <input type="password" name="password" /> <br />
      <b>Text </b> </br />
      <textarea name="text" rows="20" cols="40">{}</textarea> <br />
      <input type="submit"  value="Save" />
   </form>
    </body>
</html>
""".format(filename,filename,text))
