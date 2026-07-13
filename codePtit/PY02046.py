# Phân chia số nguyên tố 
import math
def checksonguyento(n):
    if n < 2:
        return False
    for i in range (2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    else:
        return True

n = int(input())
a = list(map(int,input().split()))
b =[]

for i in a:
    if i not in b:
        b.append(i)
d = sum(b)
t = 0
for j in range(len(b)):
    t = t + b[j]
    p = d -t
    if checksonguyento(t) and checksonguyento(p):
        print(j)
        break
else:
    print("NOT FOUND")
