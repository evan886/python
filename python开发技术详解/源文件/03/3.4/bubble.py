#!/usr/bin/python
# -*- coding: UTF-8 -*-

# xrange()
x = xrange(0,8)
print x
print x[0]
print x[7]

# 冒泡排序
def bubbleSort(numbers):                        # 冒泡算法的实现
    for j in xrange(len(numbers) - 1, -1, -1):
        for i in xrange(j):
            if numbers[i] > numbers[i+1]:       # 把数值小的数字放到顶端
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]  
            print numbers

def main():                                     # 主函数
    numbers = [23, 12, 9, 15, 6]
    bubbleSort(numbers)

if __name__ == '__main__':
    main()
