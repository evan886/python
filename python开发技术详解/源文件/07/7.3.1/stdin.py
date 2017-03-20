#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

sys.stdin = open("hello.txt", "r")
for line in sys.stdin.readlines():
    print line