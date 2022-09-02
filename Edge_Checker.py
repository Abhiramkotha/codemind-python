x,y=map(int,input().split())
ans=abs(x-y)
if ans==1 or ans==9:
    print("Yes")
else:
    print("No")