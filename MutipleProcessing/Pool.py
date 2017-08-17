import multiprocessing as mp

def job(x):
    return x**2

def multicore():
    pool = mp.Pool()
    #multiprocessing.Pool(processes=2)  assign how many cores U wanna use
    res = pool.map(job,range(10))
    #res = pool.map(job,2)  ==>error 'int' object is not iterable
    #multiprocessing.Pool.map(function,args)
    print(res)
    res = pool.apply_async(job,(2,))
    #print(res) ==>res is multiprocessing.pool.ApplyResult
    print(type(res))
    #<class 'multiprocessing.pool.ApplyResult'>
    print(res.get())

    #if we wanna put several args in multiprocessing.Pool.apply_async,we have to make it iterable
    multi_result = [pool.apply_async(job,(i,)) for i in range(10)]
    print([res.get() for res in multi_result])

if __name__=='__main__':
    multicore()
