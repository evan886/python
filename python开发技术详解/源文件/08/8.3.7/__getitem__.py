#!/usr/bin/python
# -*- coding: UTF-8 -*-

class FruitShop:
     def __getitem__(self, i):      # 获取水果店的水果
         return self.fruits[i]       

if __name__ == "__main__":
    shop = FruitShop()
    shop.fruits = ["apple", "banana"]
    print shop[1]
    for item in shop:               # 输出水果店的水果
        print item,

