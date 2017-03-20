#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Car:
    class Door:                     # 内部类
        def open(self):
            print "open door"
    class Wheel:                    # 内部类
        def run(self):
            print "car run"

if __name__ == "__main__":     
    car = Car()
    backDoor = Car.Door()           # 内部类的实例化方法一
    frontDoor = car.Door()          # 内部类的实例化方法二
    backDoor.open()
    frontDoor.open()
    wheel = Car.Wheel()
    wheel.run()




