PYI = /usr/include/python2.5

emb_1: emb_1.c
        gcc emb_1.c -g -I$(PYI) -fpic -shared -o emb_1

clean:
        rm -f emb_1 core
