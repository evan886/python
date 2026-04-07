def lines(file):
    for line in file:
        yield line 
    yield '\n'

with open('test.txt','r') as f:
    for i,line in enumerate(lines(f),1):
        print(f"{i}: {repr(line)}")
