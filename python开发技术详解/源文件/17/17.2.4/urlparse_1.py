#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urlparse

abs_urls = ["http://www.python.org","ftp://www.linux.org","http://www.gtk.org","file://"]
rel_url = "faq.html"

for abs_url in abs_urls:
    url = urlparse.urljoin(abs_url, rel_url) #拼合URL
    expected_url = url
    scheme, netloc, path, query, fragment = urlparse.urlsplit(url) #分解URL
    
    if scheme or scheme == "file":
        print url,"====> None"
        continue
    
    if scheme is not "ftp":
        expected_url = urlparse.urlunsplit(('http', netloc, path, query, fragment))
    print url,"====>",expected_url