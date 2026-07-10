# Phân chia nguyên tố 

import math
def checksonguyento(n):
    if n < 2:
        return False
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            return False
    else:
        return True
n = int(input())
a = list(map(int,input().split()))
b =[]
for x in a:
    if x not in b:
        b.append(x)
c = 0
find = False
for i in range(len(b)):
    c = c + b[i]
    d = 0
    for j in range(i +1, len(b)):
        d = d + b[j]
    if checksonguyento(c) and checksonguyento(d):
        print(i)
        find = True
        break
if find == False:
    print("NOT FOUND")


