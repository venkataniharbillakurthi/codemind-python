n=int(input())
s=0
c=1
while n>0:
    r=n%10
    s+=r
    c*=r
    n=n//10
print(abs(s-c))