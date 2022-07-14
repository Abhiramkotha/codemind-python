n=int(input())
a=[]
c=0
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
for i in a:
    f=0
    for j in range(2,i):
        if i%j==0:
            f+=1
    if f>=1:
        c+=1
print(c+1)
        