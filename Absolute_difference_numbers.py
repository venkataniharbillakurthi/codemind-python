n,l = map(int, input().split())
s = str(n)
a = int(s[:l])
b = int(s[-l::])
print(abs(a-b))