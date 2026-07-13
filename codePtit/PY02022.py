import math
def checksonguyento(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    else:
        return True
n = int(input())
a = list(map(int, input().split()))
b=[]
for i in range(len(a)):
    if checksonguyento(a[i]) and a[i] not in b:
        b.append(a[i])
for i in range (len(b)):
    c = 0
    for j in range (len(a)):
        if a[j] == b[i]:
            c = c +1
    print(b[i], c)