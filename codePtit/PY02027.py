# Tách số và sắp xếp 
z = "G07bxjq3"
n = int(input())
a = []
tmp = ""
for _ in range(n):
    s = input()
    for i in range(len(s)):
        if s[i].isdigit():
            tmp += s[i]
        else:
            if len(tmp)> 0:
                k = int(tmp)
                a.append(k)
                tmp = ""
    if len(tmp) > 0:
        z = int(tmp)
        a.append(z)
        tmp = ""
a.sort()
for i in a:
    print(i)


