s=input()
sum=0
for ch in s:
    if ch=='U':
        sum+=1
    if ch=='D':
        sum-=1
    if ch=='R':
        sum+=2
    if ch=='L':
        sum-=2
if sum==0:
    print(True)
else:
    print(False)