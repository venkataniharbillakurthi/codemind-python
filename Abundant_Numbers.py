n=int(input())
s=0
for i in range(2,n):
    if n%i==0:
        s+=i
#print(n,s)
if s>n:
    print("True")
else:
    print("False")