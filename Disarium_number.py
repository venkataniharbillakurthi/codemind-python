def disarium(n):
    res=1
    while n>0:
        rem=n%10
        res+=(rem**(len(str(n))))
        n=n//10
    return res-1

n=int(input())
if disarium(n)==n:
    print("True")
else:
    print("False")