#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Car:
    class Door:                     # �ڲ���
        def open(self):
            print "open door"
    class Wheel:                    # �ڲ���
        def run(self):
            print "car run"

if __name__ == "__main__":     
    car = Car()
    backDoor = Car.Door()           # �ڲ����ʵ��������һ
    frontDoor = car.Door()          # �ڲ����ʵ����������
    backDoor.open()
    frontDoor.open()
    wheel = Car.Wheel()
    wheel.run()




