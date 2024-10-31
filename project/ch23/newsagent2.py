#!/usr/bin/python3.9
from nntplib import NNTP, decode_header
from urllib.request import urlopen
import textwrap
import re
class NewsAgent:
    """
    An object that can distribute news items from news sources to news
    destinations.
    """    

    def __init__(self):
        self.sources = []
        self.destinations = []

    def add_source(self,source):
        self.source.append(source)
    def addDestination(self,dest):
        self.destinations.append(dest)



    def distribute(self):
        """
        Retrieve all news items from all sources, and Distribute them to all
        destinations.
        """
        items = []
        for source in self.sources:
            items.extend(source.get_items())
        for dest in self.destinations:
            dest.receive_items(items)
           
class NewsItem:

    def __init__(self,title,body):
        self.title = title 
        self.body = body 



class NNTPSource:
    """
    A news source that retrieves news items from an NNTP server.
    """
    def __init__(self,servername,group,howmany):
        self.servername = servername
        self.group = group 
        self.howmany = howmany 

    def get_items(self):
        server = NNTP(self.servername)
        resp,count, first,last, name = server.gropup(self.group)
        start = last - self.howmany + 1 
        resp,overviews = server.over((start,last))
        for id, over in overviews:
            title = decode_header(over['subject'])
            resp,info = server.body(id)
            body = '\n'.join(line.decode('utf-8')
                             for line in info.lines) + '\n\n'
            yield NewsItem(title,body)
        server.quit()

class SimpleWebSource:
    """
    A news source that retrieves news items from a web page.
    """

    def __init__(self,url,title_pattern,body_pattern,encoding='utf-8'):
        self.url = url 



class PlainDestination:
    """
    A news destination that formats all its news items as plain text.
    """
    def receive_items(self,items):
        for item in itmes:
            print(item.title)
            print('-' * len(item.title))
            print(item.body)

