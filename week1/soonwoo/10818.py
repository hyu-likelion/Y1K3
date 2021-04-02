N=int(input())

arr=map(int,input().split())

arr=list(arr)
arr.sort()

print(str(arr[0])+' '+str(arr[N-1]))
