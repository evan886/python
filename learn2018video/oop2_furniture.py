#-*- coding:utf-8 -*-
class  Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr

    def __str__(self):
        return ""

fangzi = Home(129,"三室一厅 ", "北京")
print(fangzi)
