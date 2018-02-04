#-*- coding:utf-8 -*-
temp = input("u guest")
guest = int(temp)
if guest == 8:
    print("我操，你是不是")
    print("中了，不过也没奖品")
else:
    print("错了")
print("gameover")    

'''
evan@evanpc:~/github/python/allpynotes/eg$ python 2.py 
u guest9
错了
gameover
evan@evanpc:~/github/python/allpynotes/eg$ python 2.py 
u guest8
我操，你是不是
中了，不过也没奖品
gameover
'''
