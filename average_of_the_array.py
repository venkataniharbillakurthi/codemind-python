n=int(input())
lst=list(map(int,input().split()))
es=os=0
for i in lst:
    if i%2==0:
        es+=i
    else:
        os+=i
print('{:.2f}'.format((es+os)/n))