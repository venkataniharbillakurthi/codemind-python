def sum(n):
    i = 1
    s = 0.0
    for i in range(1, n+1):
        s = s + 1/i;
    return s;
 
n = int(input())
print('{:.2f}'.format(sum(n)))