#! /usr/bin/env python
# coding:UTF-8

import os
import sys
import atexit

def daemonize(pid_file=None):
    pid = os.fork()
    if pid:
        sys.exit(0)
    os.chdir('/')
    os.umask(0)
    os.setsid()

    _pid = os.fork()
    if _pid:
        sys.exit()

    sys.stdout.flush()
    sys.stderr.flush()

    # dup2函数原子化地关闭和复制文件描述符，重定向到/dev/null ,即丢弃所有输入输出
    with open('/dev/null') as read_null, open('/dev/null', 'w') as write_null:
        os.dup2(read_null.fileno(), sys.stdin.fileno())
        os.dup2(write_null.fileno(), sys.stdout.fileno())
        os.dup2(write_null.fileno(), sys.stderr.fileno())

    if pid_file:
        with open(pid_file, 'w+') as f:
            f.write(str(os.getpid()))
            atexit.register(os.remove, pid_file)


