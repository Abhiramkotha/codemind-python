n,m=map(int,input().split())
c=0
lm=list(map(int,input().split()))
ln=list(map(int,input().split()))
for i in set(lm):
    if i not in ln:
        c+=1
for i in set(ln):
    if i not in lm:
        c+=1
print(c)
        
