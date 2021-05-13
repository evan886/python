#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
number = random.randint(1,50)
guess = 0
while True:
    num_input=input("please input one integer than is in 1 to 50")
    guess +=1
    if not num_input.isdigit():
        print("Please input interger")
    elif int(num_input) < 0 or int(num_input) >= 50:
        print("the number should be in 1  to 50")

    else:
        if number == int(num_input):
            print("ok, you ard good ,It's only %d,then you successed" % guess)
            break
        elif number > int(num_input):
            print("your number is smaller.")
        elif number < int(num_input):
            print("your number is bigger")

        else:
            print("There is  something bad, I will not wokr")
