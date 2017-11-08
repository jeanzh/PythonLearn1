from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print("process to write %s"%os.getpid())
    for i in ["A","B","c"]:
        print("put %s to queue"%i)
        q.put(i)
        time.sleep(random.random())

def read(q):
    print("process to read %s"%os.getpid())
    while True:
        value=q.get()
        print("get %s to queue"%value)
        print(value)
if __name__=="__main__":
    q=Queue()
    pw=Process(target=write,args=(q,))
  
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()



    # fibonacci
def fib(num):
    a=0
    b=1
    while num >0:
        print(b)
        t=b
        b=a+b
        a=t
        num=num-1

# file open

def openf():
    pathr="d:\\1.txt"
    with open(pathr,"r+") as f:
        print(f.read())
        f.write('Hello, world111!')

#