import math
n, k = map(int,input().split())
start = 10 **(k-1)
end = 10 ** k
c = 0
for i in range (start, end):
    if math.gcd(n, i) == 1:
        print (i, end = ' ')
        c = c + 1
        if c == 10:
            print()
            c = 0
    
