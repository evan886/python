try:
    sum = 1 + '1'
    f = open('whyfile.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print("文件出错喽:" + str(reason))
except TypeError as reason:
    print("类型出错喽:" + str(reason))
