import threading as td

def job(a,b):
    print('hello world')

if __name__=='__main__':
    t1 = td.Thread(target=job,args=(1,2))
    t1.start()
    t1.join()
