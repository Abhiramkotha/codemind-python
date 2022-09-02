t=int(input())
for j in range(t):
    n=int(input())
    i=0
    s=0
    while n>0:
        r=n%10
        s=s+(r*(2**i))
        n=n//10
        i+=1
    print(s)

    