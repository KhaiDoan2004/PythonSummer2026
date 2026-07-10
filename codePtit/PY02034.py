# Đếm các số có 2 chữ số 
s = input()
a = []
for i in range(0, len(s)-1, 2):
    so = s[i: i+2]
    a.append(so)
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    c = 0
    for j in a:
        if i == j:
            c = c + 1
    print(i,c)
