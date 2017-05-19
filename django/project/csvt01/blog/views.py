from django.shortcuts import render
from django.http import HttpResponse
def index(req):
    return HttpResponse('<h1>hellow welcome </h1>')
# Create your views here.
