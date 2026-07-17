# Ước số chung nguyên tố
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
for  _ in range (t):
    n , m = map(int, input().split())
    c  = math.gcd(n,m)
    d = 0
    while c > 0:
        d = d + c % 10 
        c = c // 10

    if checksonguyento(d):
        print("YES")
    else:
        print("NO")