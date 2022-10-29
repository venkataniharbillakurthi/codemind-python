n=int(input())
lst=list(map(int,input().split()))
os=0
for i in lst:
    if i%2!=0:
        os+=i
print(os)