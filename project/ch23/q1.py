import requests
import json
from bs4 import BeautifulSoup
import pymysql

def get_html():
    url='https://u.y.qq.com/cgi-bin/musics.fcg?-=getUCGI08231318753720207&g_tk=5381&sign=zzaerk2imozfha253e87f55eb66fc11a84b01c2d9087014&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A4%2C%22offset%22%3A0%2C%22num%22%3A20%2C%22period%22%3A%222020-08-08%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}  # 创建头部信息
    resp=requests.get(url,headers=headers)
    #print(resp.text)
    return resp.json()
def parse_html():
    lst=[]
    resp_json=get_html()
    lst_song=resp_json['detail']['data']['data']['song']
    print(lst_song)
    for item in lst_song:
        lst.append((item['rank'],item['title'],item['singerName']))
    #print(lst)
    return lst
def save_database():
    lis=parse_html()
    mydb = pymysql.connect(host="127.0.0.1", port = 3306, user = "root", passwd ="aAbc123654", database = "pythontest", charset='utf8')
    mycursor = mydb.cursor()
    sql="INSERT INTO qqmusic values (0,%s,%s,%s)"
    try:
        mycursor.executemany(sql, lis)
        print("插入成功")
        mydb.commit()
        mycursor.close()
    except Exception as e:
        print(e)
        mydb.rollback()

if __name__ == '__main__':
    save_database()
