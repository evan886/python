import sys
'''
python util.py < test_input.txt  > test_output.txt
'''
def lines(file):
        for line in file: yield line
        yield '\n'

for i in lines(sys.stdin):
       if i:
               print i
               print '---'
