from django.shortcuts import render , get_object_or_404
from .models import  BlogArticles

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return  render(request,"blog/titles.html",{"blogs":blogs})

def blog_article(request, article_id):
    #article = BlogArticles.objects.get(id= article_id)
    article = get_object_or_404(BlogArticles,id= article_id)
    pub = article.publish
    return  render(request, "blog/content.html",{"article":article,"publish":pub })

# Create your views here.
'''
In [12]:  for  blog in blogs:
    ...:     print(blog.title)
    ...:    
You raise me up

In [15]: article  =  BlogArticles.objects.get(id=1)

In [16]: article.body 
Out[16]: u'When i am  down \r\n\r\noh my soul \r\n\r\n\r\nmy hear'

In [17]: article.title 
Out[17]: u'You raise me up '

In [19]: article.auth
Out[19]: <User: evan>


In [21]: article.author.username
Out[21]: u'evan'

In [22]: article.publish 
Out[22]: datetime.datetime(2018, 2, 7, 7, 14, tzinfo=<UTC>)



'''
