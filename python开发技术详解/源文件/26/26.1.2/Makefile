PYI = /usr/include/python2.5

extend.so: extend.c
        gcc extend.c -g -I$(PYI) -fpic -shared -o extend.so

clean:
        rm -f extend.so core
