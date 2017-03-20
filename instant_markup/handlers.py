#encoding: utf-8
class Handler:
    '''
目前最好的教程详解了 by 20161108
python基础教程笔记-项目1-即时标记-Day1 
http://blog.csdn.net/miaoyunzexiaobao/article/details/43088495

    处理程序模块 调用方法的处理类,解析器在每个块的开始和结束部分调用start(),end()方法，使用合适的块名作为参数。sub()方法用于  正则表达式替换中，它会返回合适的替换函数 

很明显，若callable中的参数为函数名，则返回True，否则返回False。
判断当前类是否有对应的方法，所有的话则根据提供的额外参数使用对应方法

也就是说，若对象中有名为name(name必须是一个字符串)的属性，则返回该属性。如果对象中没有该属性，若getattr中提供了default参数，返回提供的default，否则抛出一个AttributeError错误。
很明显，若callable中的参数为函数名，则返回True，否则返回False。另外可以看到命令行中func()执行了一次。函数的执行发生在a = func()这一过程中


'    
    '''
    def callback(self,prefix,name, *args):
        method = getattr(self, prefix+name,None)
        if callable(method): return method(*args)
     #ln 28 我改过的    
    #callback的辅助方法，前缀就是start，只需要提供方法名即可    
    def start(self,name):
        self.callback('start_', name)
    #前缀为end的callback辅助方法    
    def end(self,name):
        self.callback('end_', name)
        
     #返回方法名subsutitution    
    def sub(self,name):
        def substitution(match):
            result = self.callback('sub_', name,match)
            if result is None: result= match.group(0)
            return result 
        return substitution 
    
class HTMLReaderer(Handler):
    def start_document(self):
        print '<thml><head><title>...</title></head><body>'
    def end_document(self):
        print '</body></html>'
    def start_paragraph(self):
        print '<p>'
    def end_paragraph(self):
        print '</p>'
    def start_heading(self):
        print '<h2>'
    def end_heading(self):
        print '</h2>'
    def start_list(self):
        print '<ul>'
    def end_list(self):
        print '</ul>'
    def start_listitem(self):
        print '<li>'
    def end_listitem(self):
        print '</li>'
    def start_title(self):
        print '<h1>'
    def end_title(self):
        print '</h1>'
    def sub_emphasis(self,match):
        return '<em>%s</em>' % match.group(1)
    def sub_url(self,match):
        return '<em>%s</em>' % match.group(1)
    def sub_mail(self,match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1))
    def feed(self,data):
        print data
    
        
    
