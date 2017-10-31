
# 杨辉三角

def triangles(max):
    L = [1]
    
#    while i < max:
#        print(L)
#        L = [1]+[L[i] + L[i+1] for i in range(len(L)-1)]+[1]#1 2 3 1
#        i += 1
    while max >0:
        t =[]
        yield L
        for i in range(len(L)-1):            
            t.insert(i+1,L[i]+L[i+1])
        L=[1]+t+[1]
        max= max-1
for i in triangles(7):
    print(i)