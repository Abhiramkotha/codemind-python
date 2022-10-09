n=int(input())
arr=list(map(int,input().split()))
s=len(arr)
c=0
for i in range(s):
    if(arr[i]%2!=0):
        c+=1
if(c<=2):
    print("YES")
else:
    print("NO")