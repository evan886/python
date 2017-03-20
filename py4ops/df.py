#!/usr/bin/python
#--*-- coding:utf-8 --*--
'''
下面的一个脚本利用commands模块检测磁盘使用率，标识出大于10%的磁盘（百分比可根据实际情况调整，一般设为90%，本例为了更好的说明情况，设为10%）

http://blog.csdn.net/dbanote/article/details/9414133
'''

import commands

threshold = 10
flag = False

title = commands.getoutput("df -h|head -1")

'''''
Check sda disk space usage like below format:
文件系统        容量  已用  可用 已用% 挂载点
udev            3.9G     0  3.9G    0% /dev
tmpfs           787M   26M  762M    4% /run
/dev/sda6        74G   15G   56G   21% /
tmpfs           3.9G   56M  3.8G    2% /dev/shm
tmpfs           5.0M  4.0K  5.0M    1% /run/lock
tmpfs           3.9G     0  3.9G    0% /sys/fs/cgroup
/dev/sda7       737G  362G  339G   52% /home
tmpfs           787M   16K  787M    1% /run/user/132
tmpfs           787M   72K  787M    1% /run/user/1000



evan@evanpc:~/github/python/py4ops$ df -h|grep sda
/dev/sda6        74G   15G   56G   21% /
/dev/sda7       737G  362G  339G   52% /home

evan@evanpc:~/github/python/py4ops$ df -h|grep sda|awk '{print $5}'|grep -Eo '[0-9]+'
21
52


'''

chkDiskList = commands.getoutput("df -h|grep sda").split('\n')
usedPercents = commands.getoutput("df -h|grep sda|awk '{print $5}'|grep -Eo '[0-9]+'").split('\n')

for i in range(0, len(usedPercents)):
    if int(usedPercents[i]) >= threshold:
        chkDiskList[i] += '    ----Caution!!! space usage >= ' + str(threshold)
        flag = True

'''''
Check disk space usage like below format:
/dev/mapper/backup-backup_lv
                      751G   14G  699G   2% /backup
/dev/mapper/data-data_lv
                      751G  172G  540G  25% /data
'''

chkDiskList_2 = commands.getoutput("df -h|grep -v sda|grep -v tmp|grep -v system").split('\n')
usedPercents_2 = commands.getoutput(
    "df -h|grep -v map|grep -v sda|grep -v tmp|grep -v system|awk '{print $4}'|grep -Eo '[0-9]+'").split('\n')

for i in range(0, len(usedPercents_2)):
    if int(usedPercents_2[i]) >= threshold:
        chkDiskList_2[i * 2 + 1] += '    ----Caution!!! space usage >= ' + str(threshold)
        flag = True

if flag == True:
    # combine tile, chkDiskList, chkDisklist_2
    result = [title, ]
    result.extend(chkDiskList)
    result.extend(chkDiskList_2)
    for line in result:
        print line

'''
运行结果
evan@evanpc:~/github/python/py4ops$ python df.py
文件系统        容量  已用  可用 已用% 挂载点
/dev/sda6        74G   15G   56G   21% /    ----Caution!!! space usage >= 10
/dev/sda7       737G  362G  339G   52% /home    ----Caution!!! space usage >= 10
文件系统        容量  已用  可用 已用% 挂载点
udev            3.9G     0  3.9G    0% /dev

'''