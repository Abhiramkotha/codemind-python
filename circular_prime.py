n=int(input())
f=0
for i in range(1,n+1):
    if n%i==0:
        f+=1
if f==2:
    t=0
    while n>0:
        r=n%10
        t=t*10+r
        n=n//10
    g=0
    for i in range(1,t+1):
        if t%i==0:
            g+=1
    if g==2:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
    
    