#-*- coding:utf-8 -*-
import web

urls = (
  '/', 'Index',#url地址的映射
  '/book','Book'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):#此类与‘/’地址映射
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)

class Book(object):#此类与‘/book’地址映射
    def GET(self):
        return render.book()

if __name__ == "__main__":
    app.run()
