from django.shortcuts import render
from  django.template import  loader, Context
from django.http import HttpResponse
# Create your views here.
def index(req):
    t =loader.get_template('index.html')
