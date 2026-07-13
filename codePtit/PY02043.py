n = int(input())
for _ in range(n):
    s = input()
    y = int(input())
    d = str(y)
    i = 0 
    c = 0
    while i < len(s):
        e = s[i: i+len(d)]
        so = int(e)
        if so == y:
            i = i +len(d)
            c = c+1
        else:
            i = i +1
    print(c)    