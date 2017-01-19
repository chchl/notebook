#! /usr/bin/env python
# -*-coding:UTF-8-*-

from multiprocessing import Process,Pipe
import random
def f(conn):
    for i in range(10):
        slice = random.sample(range(100), 5)
        print('send:', slice)
        conn.send(slice)
    conn.close()

if __name__ == '__main__':
    o_conn, i_conn = Pipe()
    p = Process(target = f, args=(i_conn,))
    p.start()
    for _ in range(10):
        print('receive: ',o_conn.recv())
    p.join()


