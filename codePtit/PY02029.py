# Bầu cử 
n, m = map(int,input().split())
a = list(map(int,input().split()))
b = []
d = []
for i in a:
    if i not in b:
        b.append(i)
b.sort()
for i in b:
    c = 0
    for j in a:
        if i == j:
            c = c +1
    d.append(c)
e = list(set(d))
e.sort(reverse= True)
if len(e) < 2:
    print("NONE")
else:
    for i in range(len(d)):
        if d[i] == e[1]:
            print (b[i])
            break


