n=int(input())
r=0
sp=n*n
t=0
s=0
while(n>0):
    r=r*10+n%10
    n=n//10
sq=r*r
while(sq>0):
     t=t*10+sq%10
     sq=sq//10
if(sp==t):
    print("True")
else:
    print("False")