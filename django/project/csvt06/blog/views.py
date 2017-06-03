from django.shortcuts import render
from blog.models import  Author,Book

def show_author(req):
    authors = Author.objects.all()
    
# Create your views here.
