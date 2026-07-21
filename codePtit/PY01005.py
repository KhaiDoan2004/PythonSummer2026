# Số may mắn
n = input()
a = []
for i in n:
    so = int(i)
    a.append(so)
c = a.count(4) +a.count(7)
if c == 4 or c == 7:
    print("YES")
else:
    print("NO")