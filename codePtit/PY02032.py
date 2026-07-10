# Liệt kê các số có hai chữ số tăng dần

s = input()
a = []
for i in range (0,len(s)-1,2):
    so = int(s[i:i+2])
    a.append(so)
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
b.sort()
for i in range(len(b)):
    print(b[i],end=" ")