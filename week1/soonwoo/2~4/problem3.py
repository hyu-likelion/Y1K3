str=input()
alpha="abcdefghijklmnopqrstuvwxyz"
ALPHA="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arr=[0 for i in range(len(alpha))]

for i in range(len(alpha)):
    arr[i]=arr[i]+str.count(alpha[i])+str.count(ALPHA[i])
M=max(arr)
ans=-1
for i in range(len(arr)):
    if arr[i]==M:
        if ans==-1:
            ans=i
        else:
            ans=-1
            break

if ans==-1:
    print('?')
else:
    print(ALPHA[ans])
