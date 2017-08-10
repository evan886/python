#!/usr/bin/python
#-*- coding:utf-8 -*-
from multiprocessing import  Process, Pipe
def f(conn):
    conn.send([42,None,'hello'])
    conn.close()
if __name__ == '__main__':
    paren_conn,child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(paren_conn)
    #print(paren_conn, recv())


'''
运行结果

'''

