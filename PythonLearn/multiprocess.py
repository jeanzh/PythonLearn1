from multiprocessing import pool
import os,time,random

def longtimetask(name):
    print("run task %s (%s)"%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print("task %s run %0.2f seconds"%(name,(end-start)))

if __name__=="__main__":
    print("parents process %s"%os.getpid())
    p=pool.Pool(4)
    for i in range(5):
        p.apply_async(longtimetask,args=(i,))
    print("waiting for all subprocesses done...")
    p.close()
    p.join()
    print("all subprocesses done")
