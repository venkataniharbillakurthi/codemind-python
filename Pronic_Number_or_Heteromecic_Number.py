n=int(input())
flag=0
for i in range(1,n+1):
    if i*(i+1)==n:
        flag=1
if flag==1:
    print("YES")
else:
    print("NO")