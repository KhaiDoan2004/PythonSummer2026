import math
def check3so(a, b, c):
    if a > b and b > c:
        return False
    if math.gcd(a,b) == 1 and math.gcd(b,c) == 1 and math.gcd(a,c) == 1:
        return True
n,m = map(int,input().split())
for i in range(n,m+1):
    for j in range(i+1,m+1):
        for f in range(j+1, m+1):
            if check3so(i,j,f):
                print(f"({i}, {j}, {f})")
    