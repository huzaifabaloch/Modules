"""
Currently every program execution contains a single thread known as Main 
Thread. We can create our own threads that can run in parellel. Threads are 
tasks in a single process, they are light weight and they can share variables
in a single space.
"""

import threading
import time

arr = [2, 4, 6, 8, 10]

def square(arr):
    for i in arr:
        time.sleep(1)
        print(f'SQUARE {i*i}')

def cube(arr):
    for i in arr:
        time.sleep(1)
        print(f'CUBE {i*i*i}')

# Creating two threads, that will take target function and the arguments in 
# that function.
thread1 = threading.Thread(target=square, args=(arr,))
thread2 = threading.Thread(target=cube, args=(arr,))

# In order to start threads, we need to call start method.
thread1.start()
thread2.start()

# This is saying that complete the execution of thread1 and thread2, then 
# continue with the main thread.
thread1.join()
thread2.join()

print('DONE')
