def happy(n):
    res=0
    while n>0:
        rem=n%10
        res+=(rem*rem)
        n=n//10
    if res>9:
        happy(res)
    else:
        if res==1 or res==7:
            print("True")
        else:
            print("False")

n=int(input())
happy(n)