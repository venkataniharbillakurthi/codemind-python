def square(n):
    return n*n
def reverse(n):
    n=str(n)
    n=n[::-1]
    return int(n)

n=int(input())
#print(square(n))
#print(square(reverse(n)))
print(square(n)==reverse(square(reverse(n))))