n=int(input())
n=str(n)
if n[0]=='-':
    print("-",end="")
    print(int(n[:0:-1]))
else:
    print(int(n[::-1]))