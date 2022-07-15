n,m=map(int,input().split())
ar=[]
ln=list(map(int,input().split()))
lm=list(map(int,input().split()))
for i in lm:
    if i in ln:
        if i not in ar:
            ar.append(i)
print(len(ar))