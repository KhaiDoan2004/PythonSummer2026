import math
t = int(input())
for _ in range(t):
    n = input()
    m = n[::-1]
    a = int(n)
    b = int(m)
    if math.gcd(a,b) == 1:
        print("YES")
    else:
        print("NO")
