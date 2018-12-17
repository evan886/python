#-*- coding:utf-8 -*-
class  Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area 

    def __str__(self):
        return " 房子的面积是: %d,户型是:%s 地址是 %s"  %(self.area, self.info, self.addr)
    
    def add_item(self, item):
        pass
    
class Bed:
    def __init__(self,new_name,new_area):
        self.name= new_name
        self.area = new_area

    def __str__(self):
         return "%s 占用的面积是 :%d" %(self.name, self.area)

fangzi = Home(129,"三室一厅 ", "北京")
print(fangzi)

bed1 = Bed(" 席梦思 ",4)
print(bed1)

fangzi.add_item(bed1)
print(fangzi)
