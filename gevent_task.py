import gevent
import random

def task(pid):
    gevent.sleep(random.randint(0,2))
    print('task', pid, 'done')

def synchronous():
    for i in range(1,10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)

if __name__ == '__main__':
    print 'synchronous:\n'
    synchronous()
    print 'asynchronous:\n'
    asynchronous()


