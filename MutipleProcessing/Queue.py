import multiprocessing as mp

def job(queue,a,b):
    res = 0
    res = a + b
    queue.put(res)
    #put the result into Queue

def case(queue):
    res = 0
    for i in range(100):
        res += i + i**2
    queue.put(res)

if __name__=="__main__":
    queue = mp.Queue()
    #create a Queue to store res for multiprocessing
    m1 = mp.Process(target=job,args=(queue,1,3))
    m2 = mp.Process(target=case,args=(queue,))

    m2.start()
    m1.start()  #創建線程
    m1.join()   #加入線程
    m2.join()
    print(queue.get())
    print(queue.get())
