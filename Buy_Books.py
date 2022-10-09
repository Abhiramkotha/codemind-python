import math 
n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    s=0
    su=0
    for i in range(len(a)) :
        s=s+a[i]
    for i in range(len(b)):
        su=su+b[i]
    k=su-s
    if(k>0):
        print(k)
    else:
        print("0")