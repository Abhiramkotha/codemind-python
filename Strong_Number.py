n=int(input())
temp=n
sum=0
while temp>0:
    r=temp%10
    pro=1
    for i in range(1,r+1):
        pro*=i
    sum+=pro
    temp=temp//10
if sum==n:
    print("The number %d is a strong number"%n)
else:
    print("The number %d is not a strong number"%n)
    
    