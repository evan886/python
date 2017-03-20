#!/usr/bin/python
# -*- coding: UTF-8 -*-

#µ÷ÓÃsorted()ÅÅĞò
dict = {"a" : "apple", "b" : "grape", "c" : "orange", "d" : "banana"} 
print dict   
#°´ÕÕkeyÅÅĞò  
print sorted(dict.items(), key=lambda d: d[0])
#°´ÕÕvalueÅÅĞò  
print sorted(dict.items(), key=lambda d: d[1])

#×ÖµäµÄÇ³¿½±´
dict = {"a" : "apple", "b" : "grape"} 
dict2 = {"c" : "orange", "d" : "banana"} 
dict2 = dict.copy()
print dict2


#×ÖµäµÄÉî¿½±´
import copy
dict = {"a" : "apple", "b" : {"g" : "grape","o" : "orange"}} 
dict2 = copy.deepcopy(dict)
dict3 = copy.copy(dict)
dict2["b"]["g"] = "orange"
print dict
dict3["b"]["g"] = "orange"
print dict

