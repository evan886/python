
#coding=utf-8

from django.http import HttpResponse

def index1(request):
    html = """<html>
    			  <title>Main</title>
                  <body>
                      <h1>Main Page</h1><hr>
                  </body>
              </html>"""
    return HttpResponse(html)
    

from django.shortcuts import render_to_response

entries = [ 
    {'title':'Python Portability', 'content':'Python runs on Windows, Linux/Unix, Mac OS X, OS/2, Amiga, Palm Handhelds, and Nokia mobile phones. Python has also been ported to the Java and .NET virtual machines.'},
    {'title':'Python Programming Language', 'content':'Python is a dynamic object-oriented programming language that can be used for many kinds of software development. It offers strong support for integration with other languages and tools, comes with extensive standard libraries, and can be learned in a few days. Many Python programmers report substantial productivity gains and feel the language encourages the development of higher quality, more maintainable code.'}
]

def index(request):
    return render_to_response('list_index.html', {'entries': entries})




from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from Account.models import Account

def login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    if username:
    	ac_list = Account.objects.all()
    	for ac in ac_list:
    		if ac.name == username and ac.password == password:
    			request.session['username'] = username
    username = request.session.get('username', None)
    if username:
        return render_to_response('login.html', {'username':username})
    else:
        return render_to_response('login.html')

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect("/login/")
