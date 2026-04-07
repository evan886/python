def lines(file):
    for line in file:
        yield line
    yield '\n'

with open('test.txt','r') as f:
    for line in lines(f):
        print(line)
