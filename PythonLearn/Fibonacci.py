def fib(num):
    a=0
    b=1
    while num >0:
        print(b)
        t=b
        b=a+b
        a=t
        num=num-1

