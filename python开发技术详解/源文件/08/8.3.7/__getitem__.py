#!/usr/bin/python
# -*- coding: UTF-8 -*-

class FruitShop:
     def __getitem__(self, i):      # ��ȡˮ�����ˮ��
         return self.fruits[i]       

if __name__ == "__main__":
    shop = FruitShop()
    shop.fruits = ["apple", "banana"]
    print shop[1]
    for item in shop:               # ���ˮ�����ˮ��
        print item,

