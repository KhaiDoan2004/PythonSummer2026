# Số nguyên tố lớn nhất trong ma trận 

import math
def checksonguyento(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    else: 
        return True

n, m = map(int, input().split())
matran = []
mangnguyento = []
for i in range (n):
    hang = list(map(int,input().split()))
    matran.append(hang)
for i in range (n):
    for j in range (m):
        if checksonguyento(matran[i][j]):
            mangnguyento.append(matran[i][j])
mangnguyento.sort(reverse=True)
if len(mangnguyento) == 0:
    print("NOT FOUND")
else:
    print (mangnguyento[0])
    for i in range(n):
        for j in range(m):
            if matran[i][j] == mangnguyento[0]:
                print(f"Vi tri [{i}][{j}]")


