a, k ,n = map(int,input().split())
b = k - (a % k)
c = []
while b <= n - a:
    c.append(b)
    b = b + k
if len(c) == 0:
    print(-1)
else:
    print(*c)

    
