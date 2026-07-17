import math
def checksonguyento(n):
    if n < 2:
        return False
    for i in range (2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    else:
        return True
t = int(input())
for _ in range(t):
    n = int(input())
    a =[]
    c = 0
    for i in range (1, n+1):
        if math.gcd(i,n) == 1:
            a.append(i)
    if checksonguyento(len(a)):
        print("YES")
    else:
        print("NO")
    
    
