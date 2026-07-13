# Sắp xếp nguyên tố 
import math
def checksonguyento(n):
    if n < 2:
        return False
    for i in range (2,math.isqrt(n)+1):
        if n % i == 0:
            return False
    else:
        return True
n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(len(a)):
    if checksonguyento(a[i]):
        b.append(a[i])

b.sort()
j = 0
for i in range (len(a)):
    if checksonguyento(a[i]):
        a[i] = b[j]
        j = j +1
print(*a)
