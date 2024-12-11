import os, threading, time
#
# print(os.cpu_count())
# print(os.getpid())
#
#
# def function(num):
#     time.sleep(2)
#     print(10*num)
#     print("process id: ", os.getpid())
#
#
# start = time.time()
# t1 = threading.Thread(target=function, args=(1,))
# t2 = threading.Thread(target=function, args=(2,))
# t3 = threading.Thread(target=function, args=(3,))
# t4 = threading.Thread(target=function, args=(4,))
# t5 = threading.Thread(target=function, args=(5,))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
#
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
#
# print(time.time() - start)


import multiprocessing
import os
import time


def a(num):
    time.sleep(2)
    print(f"{num} {os.getpid()}")


start = time.time()
if __name__ == "__main__":
    P1 = multiprocessing.Process(target=a, args=(2,))
    P2 = multiprocessing.Process(target=a, args=(10,))
    P1.start()
    P2.start()
    P1.join()
    P2.join()

print(time.time() - start)
