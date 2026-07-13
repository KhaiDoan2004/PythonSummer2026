# Số thuận nghịch lớn nhất trong ma trận 
def checksothuannghich(n):
    o = n
    if o < 10:
        return False
    tmp = 0 
    r = 0
    while n > 0:
        tmp = n % 10
        r = r * 10 + tmp 
        n = n // 10
    if r == o: 
        return True

n, m = map(int, input().split())
a = []
mv = 0
for i in range(n):
    hang = list(map(int,input().split()))
    a.append(hang)
for i in range(n):
    for j in range (m):
        if checksothuannghich(a[i][j]):
            if a[i][j]>mv:
                mv = a[i][j]
if mv == 0:
    print("NOT FOUND")
else:
    print(mv)
    for i in range(n):
        for j in range (m):
            if a[i][j] == mv:
                print(f"Vi tri [{i}][{j}]")

