#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template.loader import get_template
import random
from myapp.models import Product

def index(request):
    template = get_template('index.html')
    quotes = [ '今日事，今日毕','you are good ']
    html = template.render({'quote':random.choice(quotes)})
    return HttpResponse(html)

def about(request):
    template = get_template('about.html')
    quotes = [ '今日事，今日毕','you are good ','go go go ']
    html = template.render({'quote':random.choice(quotes)})
    return HttpResponse(html)

def about0(request):
    html = '''
    <html>
    <head> <title> About myself </title></head>
    <body>
    <h2>evan </2>
    <hr>
    <p>
    HI,I am evan nice to meet you!
    </p>
    
    </body>
    </html>
    '''
    return HttpResponse(html)


def listing(r):

    products = Product.objects.all()
    template = get_template('list.html')
    html = template.render({'products':products})

    return HttpResponse(html)


#随便一个str作为形参就行了 其实
def listing0(r):
    html= '''
    <html>
    <head>
     <meta charset='utf-8'>
     <title>中古手机列表</title>
    </head>
    <body>
    <h2>以下是目前本店销售中的二手 手机列表  </h2>
    <hr>
    <table width=400 border=1 bgcolor='#ccffcc'>
    {}
    </table>
    </body>
    </html>
    '''
    products = Product.objects.all()
    tags = '<tr><td>产品</td><td>售价</td><td>库存量</td></tr>'
    for p in products:
        tags = tags + '<tr><td>{}</td>'.format(p.name)
        tags = tags + '<td>{}</td>'.format(p.price)
        tags = tags + '<td>{}</td>'.format(p.qty)
    return HttpResponse(html.format(tags))



def disp_detail(request,sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的产品编号')

    template = get_template('disp.html')
    html = template.render({'product': p})

    return HttpResponse(html)



def disp_detail0(request,sku):
    html= '''
    <html>
    <head>
     <meta charset='utf-8'>
     <title>{}</title>
    </head>
    <body>
    <h2>{}</h2>
    <hr>
    <table width=400 border=1 bgcolor='#ccffcc'>
    {}
    </table>
    <a href='/list'>返回列表</a>
    </body>
    </html>
    '''

    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的产品编号')

    tags = '<tr><td>产品编号</td><td>{}</td></tr>'.format(p.sku)
    tags = tags + '<tr><td>产品名字</td><td>{}</td></tr>'.format(p.name)
    tags = tags + '<tr><td>二手售价</td><td>{}</td></tr>'.format(p.price)
    tags = tags + '<tr><td>库存数量</td><td>{}</td></tr>'.format(p.qty)
    return HttpResponse(html.format(p.name,p.name,tags))
