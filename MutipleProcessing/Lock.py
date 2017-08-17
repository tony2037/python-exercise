import multiprocessing as mp
import time

def job_no_lock(v,num):
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)

def job_lock(v,num,l):
    #key:multiprocessing.Lock().acquire() and multiprocessing.Lock().release()
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()

if __name__=='__main__':
    v = mp.Value('i',0)
    #共享內存 'i'=>'int'
    #array = mp.Array()
    l = mp.Lock()
    p1 = mp.Process(target=job_no_lock,args=(v,1,))
    p2 = mp.Process(target=job_no_lock,args=(v,3,))
    p1.start()
    p2.start()
    print('---------------No Lock---------------------')
    p1.join()
    p2.join()
    #commands below are with no Lock ==> two processes are interupt each other by  the sharing
    #3 4 7 8 11 12 12 13 13 14 17 ...

    #Let's see do the same things with multiprocessing.Lock()
    print('---------------   Lock---------------------')
    p3 = mp.Process(target=job_lock,args=(v,1,l,))
    p4 = mp.Process(target=job_lock,args=(v,3,l,))
    p3.start()
    p4.start()
    p3.join()
    p3.join()
