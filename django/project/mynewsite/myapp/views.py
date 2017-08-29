from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about(request):
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