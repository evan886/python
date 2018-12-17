#-*- coding:utf-8 -*-
from threading import  Thread
import  time

def test():
    print("-昨晚喝多了，下次少喝点-")
    time.sleep(1)

for i in range(5):
    t = Thread(target=test)
    t.start()


'''
-昨晚喝多了，下次少喝点-
-昨晚喝多了，下次少喝点-
-昨晚喝多了，下次少喝点-
-昨晚喝多了，下次少喝点-
-昨晚喝多了，下次少喝点-

'''    
