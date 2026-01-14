import requests
import json

def get_qq_music_toplist():
    url = 'https://u.y.qq.com/cgi-bin/musics.fcg?-=getucgi8633223357806146&g_tk=262966566&sign=zzarp4hakqhy6v01f51ae4be819f1a58206f8db6287c992&loginuin=3147009120&hostuin=0&format=json&incharset=utf8&outcharset=utf-8&notice=0&platform=yqq.json&neednewcode=0&data=%7B%22detail%22:%7B%22module%22:%22musictoplist.toplistinfoserver%22,%22method%22:%22getdetail%22,%22param%22:%7B%22topid%22:4,%22offset%22:0,%22num%22:20,%22period%22:%222021-02-12%22%7D%7D,%22comm%22:%7B%22ct%22:24,%22cv%22:0%7D%7D'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # 解析返回的 JSON 数据，提取排行榜信息
        song_list = data['detail']['data']['song']
        for song in song_list:
            rank = song['rank']
            song_name = song['title']
            singer_name = song['singername']
            print(f"排名: {rank}, 歌曲: {song_name}, 歌手: {singer_name}")
    else:
        print(f"请求失败，状态码: {response.status_code}")

if __name__ == "__main__":
    get_qq_music_toplist()
