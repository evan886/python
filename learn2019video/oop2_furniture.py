#-*- coding:utf-8 -*-
class  Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.contain_items = []

    def __str__(self):
        msg = " 房子的总面积是: %d,可用面积是 : %d,,户型是:%s 地址是 %s"  %(self.area,self.left_area, self.info, self.addr)
        msg += "当前房子里面的物品有%s" %(str(self.contain_items))
        return msg
    #这个属性会直接得到，不如下面的用方法,  不太明白这个item.area  c -= a 等效于c = c - a.  item 这里实例化是床
    def add_item(self, item):
        #self.left_area -=  item.area
        #self.contain_items.append(item.name) # why has name
        
        self.left_area -= item.get_area()
        self.contain_items.append(item.get_name)
class Bed:
    def __init__(self,new_name,new_area):
        self.name= new_name
        self.area = new_area

    def __str__(self):
         return "%s 占用的面积是 :%d" %(self.name, self.area)

    def get_area(self):
        return self.area

    def get_name(self):
        return self.name
     

fangzi = Home(129,"三室一厅 ", "北京")
print(fangzi)

bed1 = Bed(" 席梦思 ",4)
print(bed1)

fangzi.add_item(bed1)
print(fangzi)


bed2 = Bed("三人床 ",3)
fangzi.add_item(bed2)
print(fangzi)


'''
python3  oop2_furniture.py
如果用py2 运行是乱码的中文

 房子的总面积是: 129,可用面积是 : 129,,户型是:三室一厅  地址是 北京当前房子里面的物品有[]
 席梦思  占用的面积是 :4
 房子的总面积是: 129,可用面积是 : 125,,户型是:三室一厅  地址是 北京当前房子里面的物品有[<bound method Bed.get_name of <__main__.Bed object at 0x7f8988bcc438>>]
 房子的总面积是: 129,可用面积是 : 122,,户型是:三室一厅  地址是 北京当前房子里面的物品有[<bound method Bed.get_name of <__main__.Bed object at 0x7f8988bcc438>>, <bound method Bed.get_name of <__main__.Bed object at 0x7f8988bcc518>>]

/home/evan/python/py2018/第1章 python基础/第2节 python语法基础/07.面对对象-1/视频
18-应用 有点不明白：存放家具.flv

'''
