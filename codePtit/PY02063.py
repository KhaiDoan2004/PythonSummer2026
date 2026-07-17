# Tích lớn nhất 
n = int(input())
a = list(map(int,input().split()))
a.sort()
b = a[-1] * a[-2] * a[-3]
c = a[0] * a[1] * a[-1]
d = a[-1] * a[-2]
e = a[0] * a[1]
print(max(b,c,d,e))