from django.shortcuts import render, render_to_response
from blog.models import  Author,Book

def show_author(req):
    authors = Author.objects.all()
    return render_to_response('show_author.html',{'authors':authors})


def show_book(req):
    books = Book.objects.all()
    return render_to_response('show_book.html',{'books':books})
    
# Create your views here.
