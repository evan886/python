#!/usr/bin/python
# -*- coding: UTF-8 -*-

# xrange()
x = xrange(0,8)
print x
print x[0]
print x[7]

# ð������
def bubbleSort(numbers):                        # ð���㷨��ʵ��
    for j in xrange(len(numbers) - 1, -1, -1):
        for i in xrange(j):
            if numbers[i] > numbers[i+1]:       # ����ֵС�����ַŵ�����
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]  
            print numbers

def main():                                     # ������
    numbers = [23, 12, 9, 15, 6]
    bubbleSort(numbers)

if __name__ == '__main__':
    main()
