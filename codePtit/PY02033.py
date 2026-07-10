#Liệt kê số có 2 chữ số theo thứ tự xuất hiện
s = input()
a = []
for i in range(0,len(s)-1,2):
    so = s[i:i+2]
    a.append(so)
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
for i in range(len(b)):
    print(b[i],end=" ")