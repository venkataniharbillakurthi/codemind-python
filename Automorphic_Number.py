n=int(input())
sq=n**2
digit=sq%pow(10,len(str(n)))
if digit==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")