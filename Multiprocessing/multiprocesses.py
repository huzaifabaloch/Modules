'''
Every program execution is a default process. We can create our own processes
that can run in parelled to achieve multitasking. Processes are heavy, each of 
the process contain its own process ID and every process is separated from one
another, they cannot share variables in shared spaoce, it can be achieved by 
other way.
'''

import multiprocessing
import time

arr = [1, 2, 3, 4, 5]

def square(arr):
    for i in arr:
        time.sleep(4)
        print(i*i)

def cube(arr):
    for i in arr:
        time.sleep(4)
        print(i*i*i)

p1 = multiprocessing.Process(target=square, args=(arr, ))
p2 = multiprocessing.Process(target=cube, args=(arr, ))



if __name__ == '__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('DONE')
    