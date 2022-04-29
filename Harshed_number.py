n=int(input())
l=n
sum=0
while n!=0:
    r=n%10
    sum=sum+r
    n=n//10
if l%sum==0:
    print("True")
else:
    print("False")