# Tìm số nhỏ nhất 
n = int(input())
for _ in range(n):
    s = input()
    b = ""
    c = []
    for i in range(len(s)):
        if s[i].isdigit():
            b += s[i]
        else:
            if len(b) > 0:
                so = int(b)
                c.append(so)
                b = ""
    if len(b) > 0:
        last = int(b)
        c.append(last)
    print(min(c))
                