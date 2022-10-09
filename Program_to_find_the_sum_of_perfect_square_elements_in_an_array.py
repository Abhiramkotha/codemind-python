import math
n=int(input())
arr=list(map(int,input().split()))
s=len(arr)
su=0
for i in range(s):
    for j in range(100):
        if(arr[i]==j*j):
            su=su+arr[i]
print(su)