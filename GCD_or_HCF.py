def gcd(m,n):
    if n==0:
        return m
    else:
        return gcd(n,m%n)

m,n=map(int,input().split())
print(gcd(m,n))