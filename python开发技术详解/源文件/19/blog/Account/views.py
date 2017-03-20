#encoding=utf-8

# Create your views here.
from django.shortcuts import HttpResponse
from blog.Account.models import Account

import datetime

def index(request):
    html = "<H1>”√ªß</H1><HR>"
    return HttpResponse(html)


import datetime
def test(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)
	
import random
def random_number(request):
	body1 = "Random: %f <br />" % random.random()
	body2 = "Random: %f <br />" % random.random()
	body3 = "Random: %f <br />" % random.random()

	html = "<html><body>"+body1+body2+body3+"</body></html>"
	return HttpResponse(html)