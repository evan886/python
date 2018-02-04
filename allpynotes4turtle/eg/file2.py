#!/usr/bin/python
#-*-coding:utf8 -*-

""" func化 """
def save_file(boy,girl, count):
    # 文件的分别保存 操作
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()

f = open('record.txt')

boy = []
girl = []
count = 1

def split_file(file_name):
    for each_line in f:
        if each_line[:6] != '======':
            # 我们这里进行字符串分割操作  (role, line_spoken)? 应该不是元组呀 
            (role, line_spoken) = each_line.split(':', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)

            # 文件的分别保存 操作


            boy = []
            girl = []
            count += 1

    # 保存最好一段
    save_file(boy, girl, count)

    f.close()

split_file('record.txt')







