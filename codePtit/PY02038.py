# Đếm cặp đồng xu

n = int(input())
a = []
for i in range (n):
    hang = input()
    a.append(hang)

tong = 0
for i in range(n):
    c = 0
    for j in range (n):
        if a[i][j] =='C':
            c += 1
    tong = tong + c*(c-1)/2        
for j in range(n):
    c = 0
    for i in range (n):
        if a[i][j] =='C':
            c += 1
    tong = tong + c*(c-1)/2
print(int(tong))