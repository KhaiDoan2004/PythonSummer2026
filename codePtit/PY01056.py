# Chẵn lẽ nguyên tố 
import math
def checksonguyento(n):
    if n < 2:
        return False
    for i in range (2, math.isqrt(n)+1):
        if n % i  == 0:
            return False
    else:
        return True
t = int(input())
for _ in range (t):
    b = input()
    for i in b:
        so = int(i)
        a.append(so)
    check = True
    for i in range (0,len(a),2):
        if a[i] % 2 != 0 or a[i+1] % 2 == 0:
            check = False
            break
        else:
            check = True
    if check == True:
        print("YES")
    else:
        print("NO")