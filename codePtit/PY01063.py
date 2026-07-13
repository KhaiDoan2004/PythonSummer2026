# Đếm số trong xâu 
n = int(input())
for _ in range (n):
    s = input()
    a = int(input())
    b = str(a)
    i = 0
    c = 0
    while i < len(s):
        e = s[i: i + len(b)]
        so = int(e)
        if so == a:
            i = i + len(b)
            c = c + 1
        else:
            i = i +1
    print(c)

