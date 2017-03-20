#!/usr/bin/python
# -*- coding: UTF-8 -*-

# �ļ�������
def FileInputStream(filename):
    try:
        f = open(filename)
        for line in f:
            for byte in line:
                yield byte
    except StopIteration, e:
        f.close()
        return

# �ļ������
def FileOutputStream(inputStream, filename):
    try:
        f = open(filename, "w")
        while True:
            byte = inputStream.next()
            f.write(byte)
    except StopIteration, e:
        f.close()
        return

if __name__ == "__main__":
    FileOutputStream(FileInputStream("hello.txt"), "hello2.txt")