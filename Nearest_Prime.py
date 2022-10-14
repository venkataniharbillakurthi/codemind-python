t=int(input())
for i in range(1,t+1):
    n=int(input())
    a=n
    while True:
        is_prime = True
        for i in range(2,int(a**0.5)+1):
            if a%i == 0 :
                is_prime = False
                break
        if is_prime == True:
            break
        else:
            a += 1
    s=n
    while True:
        is_prime = True
        for i in range(2,int(s**0.5)+1):
            if s%i == 0 :
                is_prime = False
                break
        if is_prime == True:
            break
        else:
            s -= 1
    if a - n <n - s:
        print(a)
    else:
        print(s)