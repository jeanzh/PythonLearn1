from multiprocessing import Process, Queue
import os, time, random




def write(q):
    print("process to write %s"%os.getpid())
    for i in ["A","B","c"]:
        print("put %s to queue"%i)
        q.put(i)
        time.sleep(random.random())

def read():
    print("process to read %s"%os.getpid())
    while True:
        value=q.get()
        print("get %s to queue"%value)
        print(value)
    pass
if __name__=="__main__":
    q=Queue()
    pw=Process(target=write,args=(q,))
  
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
