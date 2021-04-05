T=int(input())

for i in range(T):
    arr=list(map(int,input().split()))
    N=arr[0]
    arr=arr[1:]
    avg=sum(arr)/N
    cnt=0
    for stu in arr:
        if(stu>avg):
            cnt=cnt+1
    print("%.3f" % (100*cnt/N),end='%\n')
