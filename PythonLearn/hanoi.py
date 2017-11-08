#完成汉诺塔，并打印移动步骤
#han=[[1,2,3,4],[],[]]

def move(aline,bline):
    han[bline-1].insert(0,han[aline-1][0])
    han[aline-1].pop(0)

def hanoi(aline,bline,cline,cnt):
    if cnt==1:
        move(aline,cline)
        print(han )
    else:
        hanoi(aline,cline,bline,cnt-1)
        hanoi(aline,bline,cline,1)
        hanoi(bline,aline,cline,cnt-1)
        

