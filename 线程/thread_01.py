import threading
import time


def test1(temp):
    global num
    mutex.acquire()
    for i in range(temp):
        num += 1
    mutex.release()
    print("----------test111------结果------",num)
def test2(temp):
    global num
    mutex.acquire()
    for i in range(temp):
        num += 1
    mutex.release()
    print("----------test222------结果------", num)
mutex = threading.Lock()
num =0
if __name__ == '__main__':
    t1 = threading.Thread(target=test1,args=(100,))
    t2 = threading.Thread(target=test2, args=(100,))

    t1.start()
    t2.start()

    time.sleep(2)
    print("执行完毕")

    print("num =====",num)