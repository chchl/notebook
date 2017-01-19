#!/usr/bin/env python
#-*-coding:UTF-8-*-

from multiprocessing import Pool,current_process
import os, time, sys

def worker(n):
    print('hello world', n)
    print('current process name:', current_process().name)
    time.sleep(1)

if __name__ == '__main__':
    pool = Pool(processes= 3)
    for i in range(8):
        r = pool.apply_async(worker, args=(i,))
        r.get()
    pool.close()
