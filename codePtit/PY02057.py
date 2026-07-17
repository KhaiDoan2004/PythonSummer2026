# Số may mắn trong ma trận 

n, m = map(int, input().split())
a = []

for i in range(n):
    hang = list(map(int,input().split()))
    a.append(hang)
b =[]
for i in range(n):
    for j in range(m):
        if a[i][j] not in b:
            b.append(a[i][j])
max_val = max(b)
min_val = min(b)
luck = max_val - min_val
if luck not in b:
    print("NOT FOUND")
else:
    print (luck) 
    for i in range(n):
        for j in range(m):
            if a[i][j] == luck:
                print(f"Vi tri [{i}][{j}]")



