import multiprocessing as mp
import threading as td

def job(a,b):
    print('hello world')

if __name__=="__main__":
    m1 = mp.Process(target=job,args=(1,2))
    m1.start()
    m1.join()
