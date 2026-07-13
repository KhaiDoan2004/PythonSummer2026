# Tách nhóm tối ưu 
n, k= map(int,input().split())
a = list(map(int, input().split()))
a.sort()
c = 0
for i in range(len(a)-1):
    if abs(a[i]-a[i+1]) > k:
        c = c + 1
print(c+1)