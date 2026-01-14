
# 00:19 00:48   不过是2020年的，不是最亲新的，是最新的。
# https://www.json.cn/
# pip3 install mysql-connector  not sudo  ,我用pymsql 
# find  url  network -- XHR -- musics.fcg 
#  

import requests ,pymysql 
def get_html():
    # url='https://y.qq.com/n/ryqq/toplist/4'
    url='https://u.y.qq.com/cgi-bin/musics.fcg?-=getUCGI08231318753720207&g_tk=5381&sign=zzaerk2imozfha253e87f55eb66fc11a84b01c2d9087014&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A4%2C%22offset%22%3A0%2C%22num%22%3A20%2C%22period%22%3A%222020-08-08%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'

    resp=requests.get(url) #resp 结果 是一个Response对象，包含了请求的响应内容
    # print(resp.text) string类型
    return resp.json() #返回json格式数据


#回头查看 为什么只打出一行 
# def parse_html():
#     lst = []
#     resp_json=get_html()
#     ##根据detail的建获取数值
#     lst_song=resp_json['detail']['data']['data']['song']
#      #遍历列表(获取没一手歌曲的字典)
#     for item in lst_song:
#        #print(item['rank'],item['title'],item['singerName'])
#        #(方法 (元组))
#        #lst.append((item['rank'],item['title'],item['singerName']))
#        lst.append((item['rank'],item['title'],item['singerName']))#列表存储的是所有的歌曲的元组
#        return lst 
       
#        #,item['title'],item['singerName']
    
def parse_html():
    lst=[]
    resp_json=get_html()
    lst_song=resp_json['detail']['data']['data']['song']
    #print(lst_song)
    for item in lst_song:
        lst.append((item['rank'],item['title'],item['singerName']))
    #print(lst)
    return lst


def save_database():
    mydb = pymysql.connect(host="127.0.0.1",port=3308,  user = "root", passwd ="aAbc123654", database = "pythontest", charset='utf8')
    mycursor=mydb.cursor()
    sql='insert into song_table values (%s,%s,%s)'

    val=parse_html()

    mycursor.executemany(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"record inserted.")




if __name__ == '__main__':
    # print(parse_html())
    save_database()
    # print(get_html())



# ➜  ch23 git:(master) ✗ py3 y.qq.py
# 20 record inserted.



# ySQL [pythontest]> select * from song_table ;
# +------+------------------------------+------------------------------------------+
# | id   | song_name                    | singer_name                              |
# +------+------------------------------+------------------------------------------+
# |    1 | 和你在一起                   | TFBOYS                                   |
# |    2 | 灯火                         | TFBOYS                                   |
# |    3 | 你是人间四月天 (Live)        | 邵帅                                     |
# |    4 | 孔雀                         | 任然                                     |
# |    5 | 飞鸟和蝉                     | 任然                                     |
# |    6 | 像极了 (Live)                | aZi/Lil Howcy/lil milk/连麻Swimming/Kc   |
# |    7 | Rager teenager! (Explicit)   | Troye Sivan                              |
# |    8 | 你走 (Demo)                  | 松紧先生（李宗锦）                       |
# |    9 | 烟火人间                     | 添儿呗                                   |
# |   10 | 微光海洋                     | 周深/王者荣耀                            |
# |   11 | Better with you              | 徐梦圆                                   |
# |   12 | Salt                         | Vikki Leigh                              |
# |   13 | 无人知晓                     | YU鱼                                     |
# |   14 | 余香                         | 张小九                                   |
# |   15 | 座位                         | 金池                                     |
# |   16 | 另一半                       | 金池                                     |
# |   17 | 当真                         | 野小马                                   |
# |   18 | 浪潮Vega                     | 丁于                                     |
# |   19 | 临行天                       | 伦桑                                     |
# |   20 | 破茧                         | 张韶涵                                   |
# +------+------------------------------+------------------------------------------+









# import requests
# import json
# from bs4 import BeautifulSoup
# import pymysql

# def get_html():
#     url='https://u.y.qq.com/cgi-bin/musics.fcg?-=getUCGI08231318753720207&g_tk=5381&sign=zzaerk2imozfha253e87f55eb66fc11a84b01c2d9087014&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A4%2C%22offset%22%3A0%2C%22num%22%3A20%2C%22period%22%3A%222020-08-08%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}  # 创建头部信息
#     resp=requests.get(url,headers=headers)
#     #print(resp.text)